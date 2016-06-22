#!/usr/bin/python

import sys
import base64

def xor_hex(hex1, hex2):
	bytes1 = bytearray.fromhex(hex1)
	bytes2 = bytearray.fromhex(hex2)
	n1 = len(bytes1)
	n2 = len(bytes2)
	
	if (n1<n2) :
		key = bytes1
		value = bytes2
	else:
		key = bytes2
		value = bytes1

	j = 0
	for i in range(len(value)):
		value[i] = value[i]^key[j]
		j = (j+1)%len(key)

	return value


args = sys.argv

hex1 = args[1]
hex2 = args[2]

print (xor_hex(hex1,hex2))


