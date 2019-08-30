#!bin/python

from Crypto.Hash import HMAC
from timeit import default_timer as timer

SECRET = b'toomanysecrets'
MESSAGE = b'hihello'
unknown_hmac = b'4e6bef0f59f1b08c8cab49c35a047e33'

def compute_hmac(secret, message):
    '''Compute HMAC from a given signing secret and message'''
    h = HMAC.new(secret)
    h.update(message)
    return h.hexdigest()

def nonconstant_compare(a, b):
    '''Simple nonconstant string comparison'''
    return a == b

if __name__ == '__main__':
    # print(compute_hmac(SECRET, MESSAGE))
    print(nonconstant_compare('hihello', MESSAGE))

