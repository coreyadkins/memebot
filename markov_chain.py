"""Generates a pseudo-random string of text using a markov chain language model and a text file source ."""

import random


class Markov(object):
    """Creates a class for generating random language.
    """

    def __init__(self, open_file):
        """Initiates the Markov chain.

        >>> a = Markov()
        >>> a
        'words I guess'
        """
        self.cache = {}
        self.open_file = open_file
        self.words = self.file_to_words()
        self.word_size = len(self.words)
        self.database()

    def __repr__(self):
        """Represents the Markov chain...

        >>> a = Markov()
        >>> a
        'words I guess'        """
        return 'Markov({!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.cache, self.open_file, self.words, self.word_size,
            self.database())

    def __eq__(self, other):
        """Defines equality in Markov Objects.

        >>> a = Markov()
        >>> a.word_size = 3
        >>> b = Markov()
        >>> a.word_size = 3
        >>> a == b
        True
        >>> a = Markov()
        >>> a.word_size = 3
        >>> b = Markov()
        >>> a.word_size = 5
        >>> a == b
        False
        """
        return (
            self.cache == other.cache and self.open_file == other.open_file and
            self.words == other.words and self.word_size == other.word_size and
            self.database() == other.database())

    def file_to_words(self):
        """Opens a text file and splits all the words into a list.
        """
        self.open_file.seek(0)
        data = self.open_file.read()
        words = data.split()
        return words

    def triples(self):
        """Generates triples (3-grams) from the given data string.
        """

        if len(self.words) < 3:
            return

        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i + 1], self.words[i + 2])

    def database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_top_text(self, size=(random.randrange(1, 7))):
        seed = random.randint(0, self.word_size - 3)
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)

    def generate_bottom_text(self, size=(random.randrange(1, 11))):
        seed = random.randint(0, self.word_size - 3)
        seed_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = seed_word, next_word
        gen_words = []
        for i in range(size):
            gen_words.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        gen_words.append(w2)
        return ' '.join(gen_words)