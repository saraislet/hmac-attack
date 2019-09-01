#!bin/python

from Crypto.Hash import HMAC
import timeit
from time import clock
from time import time
from time import sleep
from statistics import mean
from statistics import stdev

SECRET = b'toomanysecrets'
MESSAGE = b'hihello'

def compute_hmac(secret, message):
    h = HMAC.new(secret)
    h.update(message)
    return h.digest() 

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

def compute_most_likely_char(a, b, pos, sample_size, repeat_num):
    '''Calculate the most likely character in position pos'''
    times = [(0, 0.0)]*256  # Initialize array of times per value
    
    # Try each possible byte (256 options)
    for i in range(256):
        a[pos] = i

        # Set the callable compare, then call it with timeit
        compare = nonconstant_time_compare(a, b)
        if compare():
            times[i] = (i, 1.0)
        else:
            times[i] = (i, min(timeit.repeat(compare, timer=clock, number=sample_size, repeat=repeat_num)))

    # Sort the list of times
    times.sort(key=lambda t: t[1], reverse=True)
    return times

def find_actual(actual, sample_size, repeat_num):
    guess = bytearray(b'x' * len(actual))
    actual = bytearray(actual)
    for i in range(len(actual)):
        print("Guessing byte {}!".format(i))
        if i == len(actual) - 1:
            for j in range(256):
                guess[i] = j
                if guess == actual:
                    print("Success! Last byte is {0:2x}".format(j))
                    return guess
            print("Unsuccessful!")
            return guess
        times_and_byte = compute_most_likely_char(guess, actual, i, sample_size, repeat_num)
        times = list(map(lambda t: t[1], times_and_byte[1:256]))
        mean_time = mean(times)
        stdev_time = stdev(times)
        stdev_over = (times_and_byte[0][1] - mean_time) / stdev_time
        print("Guess is {0:02x}, actual is {1:02x}, number of stdev over others is {2:.3f}".format(times_and_byte[0][0], actual[i], stdev_over))
        guess[i] = times_and_byte[0][0]
    return guess

def print_top(vector, number):
    '''Print the top number of entries in list vector'''
    for i in range(number):
        print(vector[i])

if __name__ == '__main__':
    actual = compute_hmac(SECRET, MESSAGE)
    guess_hex = find_actual(actual, 10000, 10).hex()
    actual_hex = actual.hex()
    print("Actual is {0}, Guess is {1}".format(actual_hex, guess_hex))
