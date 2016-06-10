#!/usr/bin/python

import sys

#
# Moves a char by a numeric value, while staying between 'a' and 'z'
#

def add_key (letter, key_val):
	letter_val = ord(letter)
	val = letter_val - (key_val - ord('a'))
	if val<ord('a'):
		val = val + ord('z') - ord('a') + 1
	return val


#
# Using a string as a key, solves the Vigenere cipher of a text file
#

def vigenere(key, cipher_text):
	cipher_text = cipher_text.lower()
	clear_text = ""
	num_key = []
	for c in key.lower():
		num_key.append(ord(c))
	i = 0
	for j in range(len(cipher_text)):
		c = cipher_text[j]
		c = chr(c)
		if (ord(c) >= ord('a') and ord(c) <= ord('z')):
			c = chr(add_key(c, num_key[i]))
			i = i + 1
			if i == len(num_key):
				i=0
		clear_text = clear_text + c
	return clear_text


#
# Run the script
#

args = sys.argv

if len(args) > 1 :
	infile = args[1]
	key = args[2]
	with open(infile, "rb") as f:
		cipher_text = f.read()
		clear_text = vigenere(key, cipher_text)
		print(clear_text)


#print(chr(add_key(args[1], int(args[2]))))


