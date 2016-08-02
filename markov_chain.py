"""Generates a pseudo-random string of text using a markov chain language model and a text file source .

Sourced from the work of tedlee at github: https://github.com/tedlee/markov
"""

import random


class Markov(object):
    """Creates a class for generating random language.
    """

    def __init__(self, open_file):
        r"""Initiates the Markov chain.

        >>> a = Markov(open('test/test.txt'))
        >>> b = list(a.cache.items())
        >>> sorted(b)
        [(('This', 'is'), ['a']), (('is', 'a'), ['test.'])]
        >>> a = Markov(open('test/test.txt'))
        >>> a.words
        ['This', 'is', 'a', 'test.']
        >>> a = Markov(open('test/test.txt'))
        >>> a.word_size
        4
        """
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()

    def __repr__(self):
        """Represents the Markov chain...

        >>> a = Markov(open('test/test.txt'))
        >>> b = list(a.cache.items())
        >>> sorted(b)
        [(('This', 'is'), ['a']), (('is', 'a'), ['test.'])]
        >>> a = Markov(open('test/test.txt'))
        >>> a.words
        ['This', 'is', 'a', 'test.']
        >>> a = Markov(open('test/test.txt'))
        >>> a.word_size
        4
        """
        return 'Markov({!r}, {!r}, {!r})'.format(self.cache, self.words,
                                                 self.word_size)

    def __eq__(self, other):
        r"""Defines equality in Markov Objects.

        >>> a = Markov(open('test/test.txt'))
        >>> b = Markov(open('test/test.txt'))
        >>> a == b
        True
        >>> a = Markov(open('test/test.txt'))
        >>> b = Markov(open('test/not_test.txt'))
        >>> a == b
        False
        """
        return (self.cache == other.cache and self.words == other.words and
                self.word_size == other.word_size)

    def file_to_words(self):
        """Opens a text file and splits all the words into a list.

        >>> a = Markov(open('test/test.txt'))
        >>> a.file_to_words()
        ['This', 'is', 'a', 'test.']
        """
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words

    def triples(self):
        """Generates triples (3-grams) from the given data string.

        >>> a = Markov(open('test/test.txt'))
        >>> b = a.triples()
        >>> list(b)
        [('This', 'is', 'a'), ('is', 'a', 'test.')]
        """

        if len(self.words) < 3:
            return

        len_words = len(self.words)
        for i in range(len_words):
            yield (
                self.words[i],
                self.words[(i + 1) % len_words],
                self.words[(i + 2) % len_words]
            )

    def database(self):
        """Creates a data base of words from triples and number of words.
        """
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_text(self, size):
        """Generates a phrase from the sample text, its length is determined by size argument (an int)."""
        random.seed()
        len_words = len(self.words)
        seed = random.randint(0, len_words - 1)

        seed_word = self.words[seed]
        next_word = self.words[(seed + 1) % len_words]

        w1 = seed_word
        w2 = next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)

            try:
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])
            except KeyError:
                raise KeyError('That KeyError Again')

        gen_words.append(w2)
        return ' '.join(gen_words)
