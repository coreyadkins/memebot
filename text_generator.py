""" Opens a sample file from a .txt file, imports a markov chain class, and then uses it to generate random text."""

import markov_chain


def get_top_line(markov):
    """Generates a single string using Markov chains of 1 to 6 tokens"""
    return (markov.generate_top_text()).upper()


def get_bottom_line(markov):
    """Generates a single string using Markov chains of 1 to 11 tokens"""
    return (markov.generate_bottom_text()).upper()


def output(top, bottom, markov):
    """Returns a list of two short strings top first, bottom second."""
    meme_words = [top, bottom]
    return meme_words


def main():
    file = open('sample.txt')
    markov = markov_chain.Markov(file)
    top_line = get_top_line(markov)
    bottom_line = get_bottom_line(markov)
    return output(top_line, bottom_line, markov)


if __name__ == '__main__':
    main()
