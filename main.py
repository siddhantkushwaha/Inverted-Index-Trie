import os
import re
from pprint import pprint

from utils import get_tokens
from pytrie import trie

def index_input_files(inv_idx):
    for root, _, files in os.walk('input_files'):
        for file in files:
            
            print(f'indexing - {file}')
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r') as f:
                text = f.read()
            
            tokens = get_tokens(text)
            for i, para in enumerate(tokens, 0):
                id = f'{file_path}_para_{i}'
                for word in para:
                    count = para[word]
                    inv_idx.insert(word, id, count)

if __name__ == '__main__':
    inv_idx = trie()
    index_input_files(inv_idx)

    print(inv_idx.get_by_prefix('lorem'))

    

    