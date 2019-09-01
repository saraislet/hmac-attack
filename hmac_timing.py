#!bin/python

#from Crypto.Hash import HMAC
from timeit import timeit

SECRET = b'toomanysecrets'
MESSAGE = bytearray(b'hihello')

#def compute_hmac(secret, message):
#    h = HMAC.new(secret)
#    h.update(message)
#    return h.hexdigest()

class NonconstantTimeCompare:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a == self.b

class ConstantTimeCompare:
    def __init__(self, a, b):
        if len(a) != len(b):
            return
        self.a = a
        self.b = b

    def __call__(self):
        result = 0
        for i in range(len(self.a)):
            result |= self.a[i] ^ self.b[i]
        return result == 0

def ComputeMostLikelyChar(a, b, pos, sample_size):
    a = bytearray(a)
    b = bytearray(b)
    best = -1
    max_time = 0
    for i in range(256):
        a[pos] = i
        compare = NonconstantTimeCompare(a, b)
        result = timeit(compare, number=sample_size)
        if result > max_time:
            best = i
            max_time = result
    return best

if __name__ == '__main__':
#    print(compute_hmac(SECRET, MESSAGE))
    print(NonconstantTimeCompare(bytearray('hihello'), MESSAGE)())
    print(ConstantTimeCompare(bytearray('hihello'), MESSAGE)())
    print(NonconstantTimeCompare(bytearray('hyhello'), MESSAGE)())
    print(ConstantTimeCompare(bytearray('hyhello'), MESSAGE)())
    #print(timeit(NonconstantTimeCompare('abcd', 'bcda')))
    #print(timeit(NonconstantTimeCompare('abcd', 'acbd')))
    #print(timeit(NonconstantTimeCompare('abcd', 'abce')))
    #print(timeit(NonconstantTimeCompare('abcd', 'abcd')))
    #print(timeit(ConstantTimeCompare('abcd', 'bcda')))
    #print(timeit(ConstantTimeCompare('abcd', 'acbd')))
    #print(timeit(ConstantTimeCompare('abcd', 'abce')))
    #print(timeit(ConstantTimeCompare('abcd', 'abcd')))
    print(ComputeMostLikelyChar('abcd', 'bcda', 0, 1000000))

