#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        s_len = len(sentence)
    else:
        s_len = 0
    return (s_len, sentence if not sentence else sentence[:1])

