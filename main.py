import os
import re

import pdftotext

from utils import get_tokens
from pytrie import trie

inv_idx = trie()


def index_words(words, doc_id, text):
    for word in words:
        inv_idx.insert(word, doc_id, words[word])


def index_input_files():
    for root, _, files in os.walk('input_files'):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                tokens = None
                if file.endswith('.pdf'):
                    text = '\n'.join(pdftotext.PDF(f))
                    tokens = get_tokens(text, False)
                elif file.endswith('.txt'):
                    text = f.read().decode()
                    tokens = get_tokens(text, True)

            if tokens is not None:
                if file.endswith('.pdf'):
                    id = file_path
                    for text, para in tokens:
                        index_words(para, id, text)
                elif file.endswith('.txt'):
                    for i, (text, para) in enumerate(tokens, 0):
                        id = f'{file_path}_para_{i}'
                        index_words(para, id, text)


if __name__ == '__main__':
    inv_idx = trie()

    index_input_files()

    print(inv_idx.get_by_prefix('lorem'))
    print(inv_idx.get_by_prefix('process'))
