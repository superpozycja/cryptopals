#!python3
import sys
import base64

from Cryptodome.Util.Padding import pad, unpad

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    input = fi.read().strip().encode("utf-8")
    output = pad(input, int(sys.argv[3]))
    print(output)
    output = output.decode("utf-8")

    fo.write(output)
