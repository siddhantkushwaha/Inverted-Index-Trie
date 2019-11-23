import os
import re

from pytrie import trie

def index_input_files(inv_idx):
    for root, _, files in os.walk('input_files'):
        for file in files:
            
            print(f'indexing - {file}')
            file_path = os.path.join(root, file)
            
            with open(file_path, 'r') as f:
                text = f.read()
            words = [re.sub(r'[^a-z0-9]', '', word.lower()) for word in text.split(' ')]
            
            for word in words:
                inv_idx.insert(word, file)


if __name__ == '__main__':
    inv_idx = trie()
    index_input_files(inv_idx)

    print(inv_idx.get_by_prefix('bird'))

    

    