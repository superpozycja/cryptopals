#!/usr/bin/python3

import sys

if __name__ == "__main__":
    fi1 = open(sys.argv[1], "r")
    fi2 = open(sys.argv[2], "r")
    fo = open(sys.argv[3], "w")
    
    input = bytes(fi1.read(), "utf-8")

    key = bytes(fi2.read(), "utf-8")

    res = [input[i] ^ key[i%len(key)] for i in range(len(input))]
    res = bytes(res)
    fo.write(res.hex())
