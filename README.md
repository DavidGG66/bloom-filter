# bloom-filter
Implementation of a Bloom filter

Create a Bloom filter, add words and look them up:
```
>>> import bloomtest
>>> import bloom
>>> bf = bloom.BloomFilter(bloomtest.py_hash_bytes, 22, 2)
>>> bf.add_word("dog")
>>> bf.lookup("dog")
True
>>> bf.lookup("cat")
False
>>> bf.add_word("cat")
>>> bf.lookup("cat")
True

```

Load a dictionary of words into the Bloom filter:
```
>>> bf.load_words(bloomtest.wordfile)
>>> bf.lookup("fish")
True
>>> bf.lookup("hsif")
False
```

Get the failure rate for a Bloom filter with given parameters:
```
>>> bloomtest.test_bloom_filter(bloomtest.md5_hash, 22, 5, bloomtest.test_lex)
0.0011
```

Run tests for a range of parameters:
```
>>> bloomtest.run_tests()
Python hash function:
Hash size:  19  Hash qty:  1  Misrec rate:  0.366
Hash size:  19  Hash qty:  2  Misrec rate:  0.3485
Hash size:  19  Hash qty:  3  Misrec rate:  0.4055
Hash size:  20  Hash qty:  1  Misrec rate:  0.1967
Hash size:  20  Hash qty:  2  Misrec rate:  0.1342
Hash size:  20  Hash qty:  3  Misrec rate:  0.1183
Hash size:  21  Hash qty:  1  Misrec rate:  0.109
Hash size:  21  Hash qty:  2  Misrec rate:  0.0397
Hash size:  21  Hash qty:  3  Misrec rate:  0.022
Hash size:  22  Hash qty:  1  Misrec rate:  0.0571
Hash size:  22  Hash qty:  2  Misrec rate:  0.0119
Hash size:  23  Hash qty:  1  Misrec rate:  0.0268
Hash size:  23  Hash qty:  2  Misrec rate:  0.0026
Hash size:  24  Hash qty:  1  Misrec rate:  0.0148
Hash size:  24  Hash qty:  2  Misrec rate:  0.0005
Hash size:  25  Hash qty:  1  Misrec rate:  0.0058
Hash size:  25  Hash qty:  2  Misrec rate:  0.0002
Hash size:  26  Hash qty:  1  Misrec rate:  0.0037
Hash size:  26  Hash qty:  2  Misrec rate:  0.0

MD5 hash function:
Hash size:  19  Hash qty:  1  Misrec rate:  0.3649
Hash size:  19  Hash qty:  2  Misrec rate:  0.3459
Hash size:  19  Hash qty:  3  Misrec rate:  0.3998
Hash size:  19  Hash qty:  4  Misrec rate:  0.4841
Hash size:  19  Hash qty:  5  Misrec rate:  0.5694
Hash size:  19  Hash qty:  6  Misrec rate:  0.6575
Hash size:  20  Hash qty:  1  Misrec rate:  0.1959
Hash size:  20  Hash qty:  2  Misrec rate:  0.132
Hash size:  20  Hash qty:  3  Misrec rate:  0.1175
Hash size:  20  Hash qty:  4  Misrec rate:  0.1213
Hash size:  20  Hash qty:  5  Misrec rate:  0.1391
Hash size:  20  Hash qty:  6  Misrec rate:  0.1597
Hash size:  21  Hash qty:  1  Misrec rate:  0.1025
Hash size:  21  Hash qty:  2  Misrec rate:  0.0409
Hash size:  21  Hash qty:  3  Misrec rate:  0.0261
Hash size:  21  Hash qty:  4  Misrec rate:  0.0142
Hash size:  21  Hash qty:  5  Misrec rate:  0.0133
Hash size:  21  Hash qty:  6  Misrec rate:  0.0145
Hash size:  22  Hash qty:  1  Misrec rate:  0.0525
Hash size:  22  Hash qty:  2  Misrec rate:  0.013
Hash size:  22  Hash qty:  3  Misrec rate:  0.0043
Hash size:  22  Hash qty:  4  Misrec rate:  0.002
Hash size:  22  Hash qty:  5  Misrec rate:  0.0007
Hash size:  23  Hash qty:  1  Misrec rate:  0.0285
Hash size:  23  Hash qty:  2  Misrec rate:  0.0031
Hash size:  23  Hash qty:  3  Misrec rate:  0.0007
Hash size:  23  Hash qty:  4  Misrec rate:  0.0001
Hash size:  23  Hash qty:  5  Misrec rate:  0.0
Hash size:  24  Hash qty:  1  Misrec rate:  0.0139
Hash size:  24  Hash qty:  2  Misrec rate:  0.0011
Hash size:  24  Hash qty:  3  Misrec rate:  0.0
Hash size:  24  Hash qty:  4  Misrec rate:  0.0
Hash size:  24  Hash qty:  5  Misrec rate:  0.0
Hash size:  25  Hash qty:  1  Misrec rate:  0.007
Hash size:  25  Hash qty:  2  Misrec rate:  0.0001
Hash size:  25  Hash qty:  3  Misrec rate:  0.0
Hash size:  25  Hash qty:  4  Misrec rate:  0.0
Hash size:  25  Hash qty:  5  Misrec rate:  0.0
Hash size:  26  Hash qty:  1  Misrec rate:  0.0037
Hash size:  26  Hash qty:  2  Misrec rate:  0.0
Hash size:  26  Hash qty:  3  Misrec rate:  0.0
Hash size:  26  Hash qty:  4  Misrec rate:  0.0
```
