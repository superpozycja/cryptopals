#!/usr/bin/python3

import sys
import string

def english(s):
    letters = "etaoinsrhldcumfpgwybvkxjqz"
    freqs = [12.49, 9.28, 8.04, 7.64, 7.57, 7.23, 6.51, 6.28, 5.05, 4.07, 3.82, 3.34, 2.73, 2.51, 2.40, 2.14, 1.87, 1.68, 1.66, 1.48, 1.05, 0.54, 0.23, 0.16, 0.12, 0.09]

    res = 0
    s = s.lower()
    # i ran out of variable names
    for let in letters:
        count = s.count(let)
        ind = letters.index(let)
        if count > 0:
            res += freqs[ind]

    
    return res

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    input = bytes.fromhex(fi.read())


    max = 0
    output = ''
    for i in range(0, 0xff):
        res = bytes([x^i for x in input])
        string = res.decode("utf-8", errors='ignore')
        score = english(string)
        if score > max:
            output = string
            max = score
    fo.write(output)
