import os
import re


def get_tokens(text):
    tokens = []
    paras = text.split('\n\n')
    for para in paras:
        words = re.split(r'[ \n]', para)
        words = [re.sub(r'[^a-z0-9]', '', word.lower()) for word in words]
        words = list(filter(lambda x: len(x) > 0, words))

        word_dic = {}
        for word in words:
            word_dic[word] = word_dic.get(word, 0) + 1
        tokens.append(word_dic)
    return tokens
