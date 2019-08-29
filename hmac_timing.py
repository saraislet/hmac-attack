#!bin/python

from Crypto.Hash import HMAC

SECRET = b'toomanysecrets'
MESSAGE = b'hihello'

def compute_hmac(secret, message):
    h = HMAC.new(secret)
    h.update(message)
    return h.hexdigest()

if __name__ == '__main__':
    print(compute_hmac(SECRET, MESSAGE))

