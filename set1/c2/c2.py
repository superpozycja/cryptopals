#!/usr/bin/python3

import sys

if __name__ == "__main__":
    fi1 = open(sys.argv[1], "r")
    fi2 = open(sys.argv[2], "r")
    fo = open(sys.argv[3], "w")

    input = bytes.fromhex(fi1.read())
    key = bytes.fromhex(fi2.read())
    res = bytes([input[x]^key[x] for x in range(len(input))])
    fo.write(res.hex())
