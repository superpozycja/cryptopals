#!python3
import sys
import base64
import random

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

def oracle(ciphertext):
    # test 123

def scramble(input): 
    bef_bytes_n = random.randrange(5, 10)
    aft_bytes_n = random.randrange(5, 10)

    input = input.encode("utf-8")
    input = random.randbytes(bef_bytes_n) + input + random.randbytes(aft_bytes_n)
    input = pad(input, 16)
    
    key = random.randbytes(16)
    iv = random.randbytes(16)
    mode = AES.MODE_ECB
    if random.randrange(2) == 1:
        mode = AES.MODE_CBC
    cipher = AES.new(key, mode)
    
    scrambled = cipher.encrypt(input)
    return scrambled


if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")

    input = fi.read().strip().encode("utf-8")
    input = pad(input, 16)

    print(scramble("to jest tekst do zaszyfrowania"))


#    first_block = bytes([blocks[0][i] ^ iv[i] for i in range(16)])

#    ct = []
#    ct1 = cipher.encrypt(first_block)
#    ct.append(ct1)

#    for i in range(1, len(blocks)):
#        xord = bytes([blocks[i][x] ^ ct[i-1][x] for x in range(16)])
#        ct_block = cipher.encrypt(xord)
#        ct.append(ct_block)

#    res = b''.join(ct)
#    res = base64.b64encode(res).decode("utf-8")
#    fo.write(res)
