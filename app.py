from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Get request to EAST server.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)