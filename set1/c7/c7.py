#!python3

#^^^ im sorry for this but i broke my pycryptodome installation >~<

import sys
import base64 

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")
    
    input = fi.read().encode('utf-8')
    input = base64.b64decode(input)

    dcp = AES.new(bytes("YELLOW SUBMARINE", 'utf-8'), AES.MODE_ECB)
    output = dcp.decrypt(input)
    fo.write(output.decode("utf-8"))
