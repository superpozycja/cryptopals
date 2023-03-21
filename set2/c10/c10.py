#!python3
import sys
import base64

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    key = open(sys.argv[2], "r")
    fo = open(sys.argv[3], "w")

    input = fi.read().strip().encode("utf-8")
    input = pad(input, 16)

    blocks = []
    for i in range(0, len(input), 16):
        blocks.append(input[i:i+16])
    
    key = key.read().strip().encode("utf-8")
    key = pad(key, 16)
    key = key[0:16]
 
    iv = bytes(16)
    
    cipher = AES.new(key, AES.MODE_ECB)

    first_block = bytes([blocks[0][i] ^ iv[i] for i in range(16)])

    ct = []
    ct1 = cipher.encrypt(first_block)
    ct.append(ct1)

    for i in range(1, len(blocks)):
        xord = bytes([blocks[i][x] ^ ct[i-1][x] for x in range(16)])
        ct_block = cipher.encrypt(xord)
        ct.append(ct_block)

    res = b''.join(ct)
    res = base64.b64encode(res).decode("utf-8")
    fo.write(res)
