#!/usr/bin/python

import sys
import base64
import B64_encode.py

def xor_b64(hex1, hex2):
	bin1 = hex1.decode("hex")
	bin2 = hex2.decode("hex")

args = sys.argv

data = bytearray.fromhex(args[1])

encoded = base64.b64encode(data)

print(encoded)