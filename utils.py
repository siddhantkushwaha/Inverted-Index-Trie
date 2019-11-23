import os
import re


def get_tokens(text, split=True):
    tokens = []

    paras = re.split(r'\n.\n', text) if split else [text]
    for para in paras:
        para = re.sub(r'[^\x00-\x7F]',' ', para)
        words = re.split(r'[ \n]', para)
        words = [re.sub(r'[^a-z0-9]', '', word.lower()) for word in words]
        words = list(filter(lambda x: len(x) > 0, words))

        word_dic = {}
        for word in words:
            word_dic[word] = word_dic.get(word, 0) + 1
        tokens.append((para, word_dic))
    return tokens
