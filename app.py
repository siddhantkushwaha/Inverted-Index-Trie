import os

from flask import Flask, request, jsonify

from pytrie import trie
from main import index_file

app = Flask(__name__)


@app.route('/')
def home():
    return 'Get request to server.'


@app.route('/index', methods=['POST'])
def index():
    file_buf = request.files['file']
    
    file_name = file_buf.filename
    index_file(inv_idx, file_buf, file_name)

    with open(f'uploaded_files/{file_name}', 'wb') as f:
        file_buf.seek(0)
        f.write(file_buf.read())

    return f'Indexed. {file_name}\n'

@app.route('/word_search', methods=['GET'])
def word_search():
    query = request.args.get('query', None)
    print(query)

    results = []
    if query is not None:
        results = inv_idx.search_word(query)
        results = list(results)

    print(results)
    return jsonify(results)

@app.route('/prefix_search', methods=['GET'])
def prefix_search():
    query = request.args.get('query', None)
    print(query)

    results = []
    if query is not None:
        res = inv_idx.get_by_prefix(query)
        for word, docs in res:
            results.append((word, list(docs)))

    print(results)
    return jsonify(results)

@app.route('/clear', methods=['GET'])
def clear():
    # delete the old trie and declare a new one.
    global inv_idx
    del inv_idx
    inv_idx = trie()
    return 'Index cleared.'


if __name__ == '__main__':

    # create folder for uploaded files
    os.system('mkdir -p uploaded_files')

    # declear an inverted index, uses trie from trie.cpp
    inv_idx = trie()

    app.run(host='0.0.0.0', port=8000)
