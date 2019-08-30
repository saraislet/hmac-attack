#!bin/python

from Crypto.Hash import HMAC
from timeit import default_timer as timer

SECRET = b'toomanysecrets'
MESSAGE = b'hihello'
unknown_hmac = '4e6bef0f59f1b08c8cab49c35a047e33'


def compute_hmac(secret, message):
    '''Compute HMAC from a given signing secret and message'''
    h = HMAC.new(secret)
    h.update(message)
    return h.hexdigest()


def nonconstant_compare(a, b):
    '''Simple nonconstant string comparison'''
    return a == b


def find_hmac(hex_target):
    '''Given a target in hex, iterate hex to reach that target'''
    bite_size = len(hex_target)
    guess = ['0'] * bite_size # Initialize string

    for i in range(bite_size):
        # Iterate through each byte of the hex_target
        guess[i] = guess_byte(guess, hex_target, i)
        print('Byte ' + str(i) + ' is', guess[i])

    return ''.join(guess)


def guess_byte(guess, hex_target, position):
    '''Assuming correct bytes before position, guess byte at position'''
    return hex_target[position]


if __name__ == '__main__':
    print(find_hmac(unknown_hmac))
