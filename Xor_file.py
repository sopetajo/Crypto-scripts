#!/usr/bin/python

import sys
import base64


import binascii
filename = 'test'
with open(filename, 'rb') as f:
    content = f.read()
file = binascii.hexlify(content).decode()

outvals = xor_hex(file,"66616c6c656e")

with open("test_out", 'wb') as output:
    output.write(outvals)