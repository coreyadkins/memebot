"""Takes in image text (top text and bottom text) and an image, and returns an image with text written on it in meme
style.
"""

from PIL import Image, ImageDraw, ImageFont
from random import randint


def write_text_to_image(text_top, text_bottom, image_name):
    """Main function. Writes inputted text to image in 'meme' style"""
    image = _import_image(image_name)
    # processed_image = _process_image
    font, text_color, spacing = _determine_text_attributes()
    draw = ImageDraw.Draw(image)
    text_top_x, text_top_y, text_bottom_x, text_bottom_y = _determine_text_placement(draw, image, font, text_top,
                                                                                     text_bottom)
    _draw_image(draw, text_top, font, text_color, text_top_x, text_top_y, spacing)
    _draw_image(draw, text_bottom, font, text_color, text_bottom_x, text_bottom_y, spacing)
    _save_image(image, image_name)


def _import_image(image_name):
    """Imports selected image."""
    return Image.open(image_name)


# def _process_image(image):
#     """Eventually will hold randomized image processing.
#     """
#     return image


def _determine_text_attributes():
    """Sets attributes for proper 'meme' style text"""
    font = ImageFont.truetype('impact.ttf', 60)
    text_color = (255, 255, 255)
    spacing = 10
    return font, text_color, spacing


def _determine_text_placement(draw, image, font, text_top, text_bottom):
    """Measures image and text blocks and determines where to place each."""
    image_w, image_h = _measure_image(image)
    text_top_w, text_top_h = _measure_text(draw, text_top, font)
    text_bottom_w, text_bottom_h = _measure_text(draw, text_bottom, font)
    text_top_x, text_top_y = image_w // 2 - text_top_w // 2, image_h // 16 - text_top_h // 2
    text_bottom_x, text_bottom_y = image_w // 2 - text_bottom_w // 2,  image_h // 12 * 11 - text_bottom_h // 2
    return text_top_x, text_top_y, text_bottom_x, text_bottom_y


def _measure_image(image):
    """Outputs a tuple of the dimensions of an image."""
    return image.size


def _measure_text(draw, text, font):
    """Measures the dimensions of a block of text."""
    return draw.textsize(text, font)


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


def _save_image(image, image_name):
    """Saves image."""
    random_number = str(randint(1, 10000))
    save_name = random_number + '_' + image_name
    return image.save(save_name)