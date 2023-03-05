#!/usr/bin/python3

import sys
import string

def english(s):
    letters = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    freqs = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074, 20]

    freqs = freqs + freqs
    letters = [ ord(x) for x in letters ]

    res = 0
    for x in s:
        if x in letters:
            res += freqs[letters.index(x)%2]


    return res

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    input_all = fi.read().splitlines()
    max = 0

    output = ''
    for input in input_all:
        input = bytes.fromhex(input)
        for i in range(0, 0xff):
            res = bytes([x^i for x in input])
            score = english(res)
            if score > max:
                output = res
                max = score
    fo.write(output.decode("utf-8"))
