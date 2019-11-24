import os

from flask import Flask, request, jsonify, send_from_directory, url_for

from urllib.parse import urlparse

from pytrie import trie
from main import index_file

app = Flask(__name__, static_url_path='')


def create_link(doc_id):
    uri = urlparse(request.url)
    url = '{uri.scheme}://{uri.netloc}/'.format(uri=uri)

    if doc_id.endswith('.pdf'):
        return f'{url}files/{doc_id}'

    idx = doc_id.find('.txt')
    if idx > 1:
        return f'{url}files/{doc_id[:idx+4]}'

    return ''


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
        docs = inv_idx.search_word(query.lower())
        results = [(doc[0], doc[1], create_link(doc[0])) for doc in docs]

    print(results)
    return jsonify(results)


@app.route('/prefix_search', methods=['GET'])
def prefix_search():
    query = request.args.get('query', None)
    print(query)

    results = []
    if query is not None:
        res = inv_idx.get_by_prefix(query.lower())
        for word, docs in res:
            results.append(
                (word, [(doc[0], doc[1], create_link(doc[0])) for doc in docs]))

    print(results)
    return jsonify(results)


@app.route('/clear', methods=['GET'])
def clear():
    # delete the old trie and declare a new one.
    global inv_idx
    del inv_idx

    # clear uploaded_files directory
    os.system('rm uploaded_files/*')

    inv_idx = trie()
    return 'Index cleared.'


@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('uploaded_files', path)


if __name__ == '__main__':

    # create folder for uploaded files
    os.system('mkdir -p uploaded_files')

    # declear an inverted index, uses trie from trie.cpp
    inv_idx = trie()

    app.run(host='0.0.0.0', port=8000)
