### INCOMPLETE ###

import itertools
import os
import urllib.request
import random
from string import ascii_lowercase as letters

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

letters = list(letters)
random.shuffle(letters)
draw = letters[0:7]

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words = []
    permutations = _get_permutations_draw(draw)
    for word in permutations:
        if word in dictionary:
            words.append(word)
    return words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    i = 0
    permutations = []
    while i <= len(draw):
        permutations.append(itertools.permutations(draw, i))
        i += 1
    return permutations