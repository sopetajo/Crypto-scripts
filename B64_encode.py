#!/usr/bin/python

import sys
import base64

def decode(s):
	data = bytearray.fromhex(s)
	encoded = base64.b64encode(data)
	return encoded

args = sys.argv
in_data = args[1]
print(decode(encoded))