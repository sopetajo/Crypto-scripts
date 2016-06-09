#!/usr/bin/python

import sys

#
# Moves a char by a numeric value, while staying between 'a' and 'z'
#

def add_key (letter, key_val):
	letter_val = ord(letter)
	val = letter_val + key_val
	if val>122:
		return (val - 123 + ord('a'))
	return val


#
# Using a string as a key, solves the Vigenere cipher of a text file
#

def vigenere(key, cipher_text):
	cipher_text = cipher_text.lower()
	num_key = []
	for c in key:
		num_key.append(chr(ord(c)))
	i = 0
	for j in range(len(cipher_text)):
		c = cipher_text[j]
		if (ord(c) >= ord('a') && ord(c) <= ord('z')):
			cipher_text[j] = add_key(c, num_key[i])
			i = i + 1
			if i == num_key.len():
				i=0
	return cipher_text


#
# Run the script
#

args = sys.argv

