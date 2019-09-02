#!bin/python

from Crypto.Hash import HMAC
from datetime import datetime
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
        return a == b
    return compare

def nonconstant_time_compare_slow(a, b):
    if len(a) != len(b):
        return
    def compare():
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    return compare

def flawed_constant_time_compare(a, b):
    if len(a) != len(b):
        return
    def compare():
        result = 0
        for i in range(len(a)):
            result |= a[i] ^ b[i]
        return result == 0
    return compare

def constant_time_compare(a, b):
    if len(a) != len(b)
        return
    def compare():
        return hmac.compare_digest(a, b)
    return compare

def compute_most_likely_char(guess, actual, compare_closure_factory, pos, sample_size, repeat_num):
    '''Calculate the most likely character in position pos'''
    times = [(0, 0.0)]*256  # Initialize array of times per value
    
    # Try each possible byte (256 options)
    for i in range(256):
        guess[pos] = i

        # Set the callable compare, then call it with timeit
        compare = compare_closure_factory(guess, actual)
        if compare():
            # We randomly found the true value of actual
            times[i] = (i, 1000.0)
        else:
            times[i] = (i, min(timeit.repeat(compare, timer=clock, number=sample_size, repeat=repeat_num)))

    # Sort the list of times
    times.sort(key=lambda t: t[1], reverse=True)
    return times

def find_actual(actual, compare_closure_factory, sample_size, repeat_num, min_stdev, max_stdev, max_guesses):
    guess = bytearray(b'x' * len(actual))
    actual = bytearray(actual)
    pos = 0
    guess_counter = 0
    while True:
        guess_counter += 1
        print("Guessing byte {0} (Try {1})!".format(pos, guess_counter))
        if pos == len(actual) - 1:
            for j in range(256):
                guess[pos] = j
                if guess == actual:
                    print("Success! Last byte is {0:2x}".format(j))
                    return guess
            print("Unsuccessful!")
            pos -= 1
        times_and_byte = compute_most_likely_char(guess, actual, compare_closure_factory, pos, sample_size, repeat_num)
        times = list(map(lambda t: t[1], times_and_byte[1:256]))
        mean_time = mean(times)
        stdev_time = stdev(times)
        stdev_over = (times_and_byte[0][1] - times_and_byte[1][1]) / stdev_time
        print("Guess is {0:02x}, actual is {1:02x}, number of stdev over others is {2:.3f}".format(times_and_byte[0][0], actual[pos], stdev_over))
        if stdev_over < min_stdev or stdev_over > max_stdev:
            print("Unreasonable stdev_over, retry guess!")
            if pos > 0 and stdev_over < min_stdev:
                pos -= 1
                guess_counter = 0
            if guess_counter >  max_guesses:
                print("Giving up")
                return guess
        else:
            guess[pos] = times_and_byte[0][0]
            pos += 1
            guess_counter = 0

if __name__ == '__main__':
    timer = datetime.now()
    actual = compute_hmac(SECRET, MESSAGE)
    actual_hex = actual.hex()
    #print(str(datetime.now() - timer) + " Starting slow non constant time compare timing attack")
    #guess_hex_nc_slow = find_actual(actual, nonconstant_time_compare_slow, 1000, 20, 3, 64, 5).hex()
    #print("Actual is {0}, Slow non constant time compare guess is {1}".format(actual_hex, guess_hex_nc_slow))
    #print(str(datetime.now() - timer) + " Starting non constant time compare timing attack")
    #guess_hex_nc = find_actual(actual, nonconstant_time_compare, 10000, 100, 2, 64, 5).hex()
    #print("Actual is {0}, non constant time compare guess is {1}".format(actual_hex, guess_hex_nc))
    print(str(datetime.now() - timer) + " Starting flawed constant time compare timing attack")
    guess_hex_fc = find_actual(actual, flawed_constant_time_compare, 1000, 20, 8, 64, 5).hex()
    print("Actual is {0}, flawed constant time compare guess is {1}".format(actual_hex, guess_hex_fc))
    print(str(datetime.now() - timer) + " Starting constant time compare timing attack")
    guess_hex_c = find_actual(actual, constant_time_compare, 1000, 20, 8, 64, 5).hex()
    print("Actual is {0}, constant time compare guess is {1}".format(actual_hex, guess_hex_c))
    print(str(datetime.now() - timer) + " Finished constant time compare timing attack")

