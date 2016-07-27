"""Writes text onto an image."""

from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap


def import_image():
    return Image.open('test_image.jpg')


def write_text_to_image(image):
    font = ImageFont.truetype('impact.ttf', 60)
    shadowcolor = (0, 0, 0)
    textcolor = (255, 255, 255)
    x, y = 10, 10
    text = 'NOT SURE IF \n THIS THING WORKS' # Setup File IO for text
    spacing = 300 #Use wrap to determine spacing?
    draw = ImageDraw.Draw(image)
    draw.multiline_text((x-3, y-3), text, font=font, fill=shadowcolor, spacing=spacing)
    draw.multiline_text((x+3, y-3), text, font=font, fill=shadowcolor, spacing=spacing)
    draw.multiline_text((x-3, y+3), text, font=font, fill=shadowcolor, spacing=spacing)
    draw.multiline_text((x+3, y+3), text, font=font, fill=shadowcolor, spacing=spacing)
    draw.multiline_text((x, y), text, fill=textcolor, font=font, spacing=spacing)
    return image

def save_image(image):
    return image.save('test_meme.jpg')

def main():
    """"""
    image = import_image()
    memed_image = write_text_to_image(image)
    save_image(memed_image)


if __name__ == '__main__':
    main()
