#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        char = None
    else:
        char = sentence[0]
    output = (leng, char)
    return (output)
