#!/usr/bin/python3

import sys
import base64 as b64

if __name__ == "__main__":
    fi = open("input", "r")
    fo = open("output", "w")
    input = bytes.fromhex(fi.read())
    output = b64.b64encode(input)
    fo.write(output.decode("utf-8"))
