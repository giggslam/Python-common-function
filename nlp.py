from collections import Counter

def count_ngrams(lines, min_length=2, max_length=4):
    lengths = range(min_length, max_length + 1)
    ngrams {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen(max_length))

