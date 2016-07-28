""" Opens a sample file from a .txt file, imports a markov chain class, and then uses it to generate random text.

Sourced from the work of tedlee at github: https://github.com/tedlee/markov
"""

import markov_chain
import random


def get_top_line(markov):
    """Generates a single string using Markov chains of 1 to 6 tokens"""
    size = (random.randrange(1, 7))
    return (markov.generate_text(size)).upper()


def get_bottom_line(markov):
    """Generates a single string using Markov chains of 1 to 10 tokens"""
    size = (random.randrange(1, 11))
    return (markov.generate_text(size)).upper()


def generate_text():
    file = open(input/corpus.txt)
    markov = markov_chain.Markov(file)
    top_line = get_top_line(markov)
    bottom_line = get_bottom_line(markov)
    return top_line, bottom_line
