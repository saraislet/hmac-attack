#!bin/python

#from Crypto.Hash import HMAC
from timeit import timeit
from time import clock
from time import time
from time import sleep

SECRET = b'toomanysecrets'
MESSAGE = bytearray(b'hihello')

#def compute_hmac(secret, message):
#    h = HMAC.new(secret)
#    h.update(message)
#    return h.hexdigest()

def nonconstant_time_compare(a, b):
    if len(a) != len(b):
        return
    def compare():
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
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
    times = [(0, 0.0)]*256
    for i in range(256):
        a[pos] = i
        compare = nonconstant_time_compare(a, b)
        result = timeit(compare, timer=clock, number=sample_size)
        times[i] = ((i, result))
    def get_time(t):
        return t[1]
    times.sort(key=get_time, reverse=True)
    return times

def find_actual(actual, sample_size):
    guess = bytearray(b'x' * len(actual))
    actual = bytearray(actual)
    for i in range(len(actual)):
        times = compute_most_likely_char(guess, actual, i, sample_size)
        guess[i] = times[0][0]
    return guess

def print_top(vector, number):
    for i in range(number):
        print(vector[i])

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
    guess = bytearray(b'abcd')
    actual = bytearray(b'qwer')
    print(find_actual(actual, 500000))
    times = compute_most_likely_char(guess, actual, 0, 100000)
    print(timeit("bytearray(b'abcd') == bytearray(b'qwer')"))
    print(timeit(nonconstant_time_compare(guess, actual)))
    print(guess[0])
    print(actual[0])
    print_top(times, 25)

