#!/usr/bin/python3

import sys
import base64

def bit_count(n):
    return sum(b=='1' for b in bin(n))

def ham(a, b):
    if len(b) < len(a):
        a, b = b, a
    
    return sum([bit_count(a[i] ^ b[i]) for i in range(len(a))])

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

    input_all = fi.read().replace('\n', '')

    input_all = input_all.encode('ascii')
    input_all = base64.b64decode(input_all)

    pairs = []

    for ksize in range(2, 50):
        dis = 0
        it = 0
        for i in range(0, len(input_all), ksize):
            it = it+1
            dis += ham(input_all[i:i+ksize], input_all[i+ksize:i+2*ksize])/ksize
        pairs.append((ksize, dis/it))

    pairs.sort(key = lambda a : a[1])

    best_blocks = []
    best_key = [] 
    best_score = 0

    for bpair in pairs[0:5]:
        bkey = bpair[0]
        blocks = []
        for i in range(0, len(input_all), bkey):
            blocks.append(input_all[i:i+bkey]);
        blocks2 = blocks[:-1]

        chunks = []

        for i in range(bkey):
            tmp = []
            for b in blocks2:
                tmp.append(b[i].to_bytes(1, 'big'))
            tmp = b''.join(tmp)
            chunks.append(tmp)

        
        tmp_score = 0
        key_all = []
        for chunk in chunks:
            max = 0
            output = ''
            ch_key = 0
            for i in range(0, 0xff):
                res = bytes([x^i for x in chunk])
                score = english(res)
                if score > max:
                    output = res
                    max = score
                    ck_key = i
            tmp_score += max
            key_all.append(ck_key)

        if tmp_score > best_score:
            best_blocks = blocks
            best_key = key_all
            best_score = tmp_score

    res = b''.join(best_blocks)
    res = [res[i] ^ best_key[i%len(best_key)] for i in range(len(res))]
    res = bytes(res).decode('utf-8')
    fo.write(res)

#    fo.write(output.decode("utf-8"))
