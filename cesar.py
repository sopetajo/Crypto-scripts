#!/usr/bin/python

import sys
import operator

#
# Get the post frequent byte in a file
#
def solveCesar(inFile):
	freqs = {}
	with open(inFile, "rb") as f:
		byte = f.read(1)
		byte = byte.encode('hex')
		while byte != "":
			if freqs.has_key(byte):
				freqs[byte] += 1
			else:
				freqs[byte] = 1
			byte = f.read(1)
			byte = byte.encode('hex')
	magicByte = max(freqs.iteritems(), key=operator.itemgetter(1))[0]
	return (int(magicByte, 16) - int("65", 16))
	

#
# Rotate bytes by n
#	
def clearText(inFile, n):
	with open(inFile, "rb") as f:
		byte = f.read(1)
		byte = byte.encode('hex')
		outStr = ""
		while byte != "":
			outByte = (int(byte, 16) - n) % 256
			outByte = chr(outByte)
			outStr = outStr + outByte
			byte = f.read(1)
			byte = byte.encode('hex')
		print outStr


#
# Run the script
#        
args = sys.argv

if len(args) > 1 :
	n = solveCesar(args[1])
	i = int(args[2])
	#for i in range(256):
	clearText(args[1], i)
