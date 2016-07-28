"""Main."""

from text_generator import generate_text
from image_writer import write_text_to_image
from PIL import Image
from random import randint


def save_image(image, image_name):
    output_name = str(image_name).replace('data/', '')
    output_name = str(randint(1, 10000)) + output_name
    image.save('output/' + output_name)


def main():
    top_line, bottom_line = generate_text()
    image, image_name = write_text_to_image(top_line, bottom_line, 'data/futurama_fry.jpg')
    save_image(image, image_name)


if __name__ == '__main__':
    main()