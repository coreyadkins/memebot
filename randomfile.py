""" Functions to input or output a random file image path."""

from os.path import splitext, join
import os
import random
from tempfile import mkstemp


def get_random_output_path(filename, dirname='output'):
    """ Appends a random string to a filename while preserving the extension

    :return str: directory/basename.r4Nd0Ms7r!n9.webm
    >>> '/basename.' in get_random_output_path('basename.webm')
    True
    """
    basename, ext = splitext(filename)
    handle, path = mkstemp(ext, basename + '.', dirname, '')
    os.unlink(path)
    return path


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
