""" Opens a sample file from a .txt file, imports a markov chain class, and then uses it to generate random text."""


import markov_chain


def output(markov):
    top = (markov.generate_top_text()).capitalize()
    bottom = (markov.generate_bottom_text()).capitalize()
    meme_words = [top, bottom]
    print(meme_words)

def main():
    file = open('sample.txt')
    markov = markov_chain.Markov(file)
    output(markov)

if __name__ == '__main__':
    main()