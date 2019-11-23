import os
import re

import pdftotext

from utils import get_tokens
from pytrie import trie


def index_words(inv_idx, words, doc_id, text):
    for word in words:
        inv_idx.insert(word, doc_id, words[word])


def index_file(inv_idx, file_buf, file_name):
    tokens = None
    if file_name.endswith('.pdf'):
        text = '\n'.join(pdftotext.PDF(file_buf))
        tokens = get_tokens(text, False)
    elif file_name.endswith('.txt'):
        text = file_buf.read().decode()
        tokens = get_tokens(text, True)

    if tokens is not None:
        if file_name.endswith('.pdf'):
            id = file_name
            for text, para in tokens:
                index_words(inv_idx, para, id, text)
        elif file_name.endswith('.txt'):
            for i, (text, para) in enumerate(tokens, 0):
                id = f'{file_name}_para_{i}'
                index_words(inv_idx, para, id, text)


def index_input_files(inv_idx):
    for root, _, files in os.walk('input_files'):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

            with open(file_path, 'rb') as f:
                index_file(inv_idx, f, file_path)


if __name__ == '__main__':
    inv_idx = trie()
    index_input_files(inv_idx)

    print(inv_idx.get_by_prefix('lorem'))
    print(inv_idx.get_by_prefix('process'))
