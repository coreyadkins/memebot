"""Writes 'meme' text onto an image. Pass in image name and location, top text, bottom text, and name of the file to
save.
"""

from PIL import Image, ImageDraw, ImageFont


def _import_image():
    """Imports selected image."""
    return Image.open('test_image.jpg')


def _write_text_to_image(image):
    """Writes inputted text to image in 'meme' style"""
    text_top = 'NOT SURE IF SINCERE'
    text_bottom = 'OR JUST SARCASM'
    font = ImageFont.truetype('impact.ttf', 60)
    text_color = (255, 255, 255)
    image, image_w, image_h = _process_image(image)
    draw = ImageDraw.Draw(image)
    text_top_w, text_top_h = draw.textsize(text_top, font)
    text_bottom_w, text_bottom_h = draw.textsize(text_bottom, font)
    spacing = 10
    text_top_x, text_top_y = image_w // 2 - text_top_w // 2, image_h // 16 - text_top_h // 2
    _draw_image(draw, text_top, font, text_color, text_top_x, text_top_y, spacing)
    text_bottom_x, text_bottom_y = image_w // 2 - text_bottom_w // 2,  image_h // 12 * 11 - text_bottom_h // 2
    _draw_image(draw, text_bottom, font, text_color, text_bottom_x, text_bottom_y, spacing)
    return image


def _process_image(image):
    """Measures image for text placement.

    Eventually will hold randomized image processing.
    """
    image_w, image_h = image.size
    return image, image_w, image_h


def _draw_image(draw, text, font, text_color, x, y, spacing):
    """Draws text to image."""
    _add_border_to_text(draw, x, y, text, font, spacing)
    draw.multiline_text((x, y), text, fill=text_color, font=font, spacing=spacing)


def _add_border_to_text(draw, x, y, text, font, spacing):
    """Adds black border to text."""
    border_color = (0, 0, 0)
    draw.multiline_text((x - 3, y - 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text((x + 3, y - 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text((x - 3, y + 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text((x + 3, y + 3), text, font=font, fill=border_color, spacing=spacing)


def _save_image(image):
    """Saves image."""
    return image.save('test_meme.jpg')


def main():
    """"""
    image = _import_image()
    memed_image = _write_text_to_image(image)
    _save_image(memed_image)


if __name__ == '__main__':
    main()
