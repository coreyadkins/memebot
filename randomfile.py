""" Selects some random stuff """

from os.path import splitext, join
import os
import random


def get_unique_str(str_length=12):
    """ Generate a random alphanumeric string (36^str_length permutations)

    :return str: unique_string
    """
    VALID_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'
    random.seed()

    unique = ''
    for i in range(str_length):
        idx = random.randrange(0, len(VALID_CHARS))
        unique += VALID_CHARS[idx]

    return unique


def get_random_output_path(filename, dir = 'output'):
    """ Appends a random string to a filename while preserving the extension

    :return str: directory/basename.1234567890Ab.webm
    """
    basename, ext = splitext(filename)
    rando = get_unique_str()

    return join(dir, '{}/{}.{}{}'.format(dir, basename, rando, ext))


def get_random_input_file(dir='input', extensions='.jpg'):
    """ Choose a file of given extension(s) at random from the selected directory

    :return str:
    """
    exts = extensions.split(',')
    files = [file for file in os.listdir(dir) if file[-4:] in exts]
    random.shuffle(files)
    return join(dir, files.pop())


def main():
    """ main """
    print(get_random_output_path('dad.jpg'))
    print(get_random_input_file())


if __name__ == '__main__':
    main()
