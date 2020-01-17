#
# Test code for Bloom filter
#

from hashlib import md5
from random import randint
from bloom import BloomFilter

#
# Define hash functions
#

def int_to_bytes(x, size):
    """
    Put an integer into a bytes object of a given size
    """
    mask = (2 ** (size * 8)) - 1
    uns_x = x & mask
    return uns_x.to_bytes(size, 'big')

def py_hash_bytes(x):
    """
    Return an 8-byte hash value based on Python 'hash' function
    """
    return int_to_bytes(hash(x), 8)

def md5_hash(x):
    """
    Return a 16-byte MD5 hash value
    """
    return md5(x.encode('utf-8')).digest()


wordfile = '/usr/share/dict/words'
    

def test_recall(bf, filename):
    """
    Make sure a Bloom filter will find every word added to it
    """
    bf.load_words(filename)
    good_recall = True
    with open(wordfile) as f:
        for line in f:
            if not bf.lookup(line.strip()):
                good_recall = False
    if good_recall:
        print("Recall is good")
    else:
        print("Recall failed")


def rand_word():
    """
    Generate a string of 5 random characters, perhaps capitalized
    """
    if randint(0, 1):
        word = chr(randint(97, 122))
    else:
        word = chr(randint(65, 90))

    for i in range(4):
        word += chr(randint(97, 122))

    return word


def test_bloom_filter(hash_fn, hash_size, hash_qty, lex):
    """
    Build a Bloom filter and test its precision
    """
    bf = BloomFilter(hash_fn, hash_size, hash_qty)
    bf.load_words(wordfile)
    
    # check precision
    prec_fails = 0
    for i in range(10000):
        word = rand_word()
        if bf.lookup(word) and not word in lex:
            prec_fails += 1

    return prec_fails / 10000


def lex_set(filename):
    """
    Make a set of words by reading them from a file. Assumes each line contains
    a single word.
    """
    ret = set()
    with open(filename) as f:
        for line in f:
            ret.add(line.strip())
    return ret


test_lex = lex_set(wordfile)

def run_tests():
    """
    Check the precision for Bloom filters with various parameters
    """
    print("Python hash function:")
    for hash_size in range(19, 27):
        for hash_qty in range(1, int(64/hash_size)+1):
            prec = test_bloom_filter(py_hash_bytes, hash_size, hash_qty, test_lex)
            print("Hash size: ", hash_size, " Hash qty: ", hash_qty, " Misrec rate: ", prec)

    print()
    print("MD5 hash function:")
    for hash_size in range(19, 27):
        for hash_qty in range(1, int(128/hash_size)+1):
            prec = test_bloom_filter(md5_hash, hash_size, hash_qty, test_lex)
            print("Hash size: ", hash_size, " Hash qty: ", hash_qty, " Misrec rate: ", prec)
