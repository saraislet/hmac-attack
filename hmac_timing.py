#!bin/python

from Crypto.Hash import HMAC

secret = b'toomanysecrets'
message = b'hihello'

h = HMAC.new(secret)
h.update(message)
print(h.hexdigest())

