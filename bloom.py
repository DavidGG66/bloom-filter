#
#  Bloom filter implementation
#

class BloomFilter():
    """
    Implements a Bloom filter as for a spell-check dictionary.

    Contains a hash function, which returns a master hash value as a bytes
    object when given a word (string). This master value is divided into a
    number of different independent values, each of which corresponds to a bit
    in the bytearray which makes up the Bloom filter's main data structure.

    Along with the hash function, a hash_size is specified. This is the size
    of each independent hash value, in bits. This determines the size of the
    bytearray as well.

    Contains a hash_qty as well, which is a maximum number of independent hash
    values to use, if you only want to use part of the master value
    """

    def __init__(self, hash_fn, hash_size, hash_qty):

        hash = hash_fn("test")
        if type(hash) is not bytes:
            raise ValueError("Hash must return a bytes object")
        else:
            self.hash_fn = hash_fn
        
            self.hash_size = hash_size
            addressable_bytes = 2 ** max(hash_size - 3, 1)
            self.lex = bytearray(addressable_bytes)
            self.mask = (2 ** hash_size) - 1

            self.hash_qty = hash_qty


    def hash_indices(self, word):
        """
        Return a set of indices into the self.lex bytearray from a word.

        Get an index by looking at the 'hash_size' right-most bits of the
        master hash value; Shift the master value right by 'hash_size' and
        repeat until there aren't enough bits left, or you've gotten the
        max quantity of independent hashes.

        Each index has two parts: an index into the bytearray to find the right
        byte, and an index into that byte to find the right bit
        """
        hash_bytes = self.hash_fn(word)
        hash_int = int.from_bytes(hash_bytes, 'big')

        bit_size = len(hash_bytes) * 8
        qty_left = self.hash_qty
        indices = []
        while bit_size >= self.hash_size and qty_left > 0:
            index = hash_int & self.mask
            byte_idx, bit = divmod(index, 8)
            indices.append((byte_idx, 1 << bit))
            hash_int >>= self.hash_size
            bit_size -= self.hash_size
            qty_left -= 1

        return indices

        
    def add_word(self, word):
        """
        Add a word to the Bloom filter
        """
        if type(word) != str:
            print("Cannot add ", type(word), " to the Bloom filter")
        else:
            for byte_idx, bit_idx in self.hash_indices(word):
                self.lex[byte_idx] |= bit_idx

    
    def load_words(self, filename):
        """
        Add words from a file to the Bloom filter. Assumes each line contains
        a single word.
        """
        with open(filename) as f:
            for line in f:
                self.add_word(line.strip())


    def lookup(self, word):
        """
        Look a word up in the Bloom filter
        """
        if type(word) != str:
            print(type(word), " not in the Bloom filter")
            return False
        
        for byte_idx, bit_idx in self.hash_indices(word):
            if not self.lex[byte_idx] & bit_idx:
                return False

        return True
