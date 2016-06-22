#!/usr/bin/python

import sys
import gmpy2 as gmpy
from Crypto.PublicKey import RSA

args = sys.argv

p = int(args[1])
q = int(args[2])
e = int(args[3])

n = p*q

d = int(gmpy.invert(e,(p-1)*(q-1)))

key = RSA.construct((n,e,d))

print(key.exportKey())
