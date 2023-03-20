#!python3

#^^^ im sorry for this but i broke my pycryptodome installation >~<

import sys
import base64 

if __name__ == "__main__":
    fi = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "w")
    
    input = fi.read().split()
    
    worst = []
    worst_sc = 0
    for line in input:
        chunks = []
        for i in range(0, len(line), 0x10):
            chunks.append(line[i:i+0x10])
        chunks.sort()
        score = 0
        for i in range(len(chunks)-1):
            if chunks[i] == chunks[i+1]:
                score += 1
        
        if score > worst_sc:
            worst_sc = score
            worst = line

    fo.write(worst)
