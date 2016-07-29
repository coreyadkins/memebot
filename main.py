"""Main."""

from text_generator import generate_text
from image_writer import write_text_to_image
from PIL import Image
from random import randint
from os import path, makedirs
from randomfile import get_random_input_file


def save_image(image, image_name):
    output_name = str(image_name).replace('input/', '')
    output_name = str(randint(1, 10000)) + output_name
    if not path.exists('output'):
        makedirs('output')
    image.save('output/' + output_name)


def main():
    top_line, bottom_line = generate_text()
    image_name = get_random_input_file()
    image = write_text_to_image(top_line, bottom_line, image_name)
    save_image(image, image_name)


if __name__ == '__main__':
    main()