#!bin/python

#from Crypto.Hash import HMAC
from timeit import timeit
from time import clock
from time import time

SECRET = b'toomanysecrets'
MESSAGE = bytearray(b'hihello')

#def compute_hmac(secret, message):
#    h = HMAC.new(secret)
#    h.update(message)
#    return h.hexdigest()

def nonconstant_time_compare(a, b):
    def compare():
        return a == b
    return compare

def constant_time_compare(a, b):
    if len(a) != len(b):
        return
    def compare():
        result = 0
        for i in range(len(a)):
            result |= a[i] ^ b[i]
        return result == 0
    return compare

def compute_most_likely_char(a, b, pos, sample_size):
    a = bytearray(a)
    b = bytearray(b)
    best = -1
    max_time = 0
    for i in range(256):
        a[pos] = i
        compare = nonconstant_time_compare(a, b)
        result = timeit(compare, timer=clock, number=sample_size)
        if result > max_time:
            best = i
            max_time = result
    return best

if __name__ == '__main__':
#    print(compute_hmac(SECRET, MESSAGE))
    print(nonconstant_time_compare(bytearray(b'hihello'), MESSAGE)())
    print(constant_time_compare(bytearray(b'hihello'), MESSAGE)())
    print(nonconstant_time_compare(bytearray(b'hyhello'), MESSAGE)())
    print(constant_time_compare(bytearray(b'hyhello'), MESSAGE)())
    #print(timeit(NonconstantTimeCompare('abcd', 'bcda')))
    #print(timeit(NonconstantTimeCompare('abcd', 'acbd')))
    #print(timeit(NonconstantTimeCompare('abcd', 'abce')))
    #print(timeit(NonconstantTimeCompare('abcd', 'abcd')))
    #print(timeit(ConstantTimeCompare('abcd', 'bcda')))
    #print(timeit(ConstantTimeCompare('abcd', 'acbd')))
    #print(timeit(ConstantTimeCompare('abcd', 'abce')))
    #print(timeit(ConstantTimeCompare('abcd', 'abcd')))
    print(compute_most_likely_char(b'abcd', b'bcda', 0, 1000))

