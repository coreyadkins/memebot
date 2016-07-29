"""Takes in image text (top text and bottom text) and an image, and returns an image with text written on it in meme
style.
"""

from PIL import Image, ImageDraw, ImageFont

TEXT_COLOR = (255, 255, 255)
SPACING = 5


def write_text_to_image(text_top, text_bottom, image_name):
    """Main function. Writes inputted text to image in 'meme' style"""
    image = _import_image(image_name)
    # processed_image = _process_image
    draw = ImageDraw.Draw(image)
    normal_font = ImageFont.truetype('impact.ttf', 50)
    text_top, text_bottom, top_font, bottom_font = _fit_text_to_image(
        image, text_top, text_bottom, draw, normal_font)
    text_top_x, text_top_y, text_bottom_x, text_bottom_y = _determine_text_placement(
        draw, image, top_font, bottom_font, text_top, text_bottom)
    _draw_image(draw, text_top, top_font, TEXT_COLOR, text_top_x, text_top_y,
                SPACING)
    _draw_image(draw, text_bottom, bottom_font, TEXT_COLOR, text_bottom_x,
                text_bottom_y, SPACING)
    return image, image_name


def _import_image(image_name):
    """Imports selected image."""
    return Image.open(image_name)

# def _process_image(image):
#     """Eventually will hold randomized image processing.
#     """
#     return image


def _determine_text_placement(draw, image, top_font, bottom_font, text_top,
                              text_bottom):
    """Measures image and text blocks and determines where to place each."""
    image_w, image_h = _measure_image(image)
    text_top_w, text_top_h = _measure_text(draw, text_top, top_font, SPACING)
    text_bottom_w, text_bottom_h = _measure_text(draw, text_bottom,
                                                 bottom_font, SPACING)
    text_top_x, text_top_y, text_bottom_x, text_bottom_y = _calculate_coords(
        image_w, image_h, text_top_w, text_top_h, text_bottom_w, text_bottom_h)
    return text_top_x, text_top_y, text_bottom_x, text_bottom_y


def _calculate_coords(image_w, image_h, text_top_w, text_top_h, text_bottom_w,
                      text_bottom_h):
    """Inputs image and text block dimensions and returns top-left x and y coordinates for placement of both texts.

    >>> _calculate_coords(100, 100, 10, 5, 15, 5)
    (45, 4, 43, 86)
    >>> _calculate_coords(100, 100, 10, 30, 15, 30)
    (45, 5, 43, 65)
    """
    text_top_x, text_top_y = image_w // 2 - text_top_w // 2, image_h // 16 - text_top_h // 2
    text_bottom_x, text_bottom_y = image_w // 2 - text_bottom_w // 2, image_h // 12 * 11 - text_bottom_h // 2
    if text_top_y < 0:
        text_top_y = SPACING
    if text_bottom_y + text_bottom_h > image_h:
        overage = (text_bottom_y + text_bottom_h) - image_h + SPACING
        text_bottom_y -= overage
    return text_top_x, text_top_y, text_bottom_x, text_bottom_y


def _measure_image(image):
    """Outputs a tuple of the dimensions of an image."""
    return image.size


def _measure_text(draw, text, font, spacing):
    """Measures the dimensions of a block of text."""
    return draw.multiline_textsize(text, font, spacing)


def _draw_image(draw, text, font, text_color, x, y, spacing):
    """Draws text to image."""
    _add_border_to_text(draw, x, y, text, font, spacing)
    draw.multiline_text(
        (x, y), text, fill=text_color, font=font, spacing=spacing)


def _add_border_to_text(draw, x, y, text, font, spacing):
    """Adds black border to text.

    Sourced from Alec Bennett at https://mail.python.org/pipermail/image-sig/2009-May/005681.html
    """
    border_color = (0, 0, 0)
    draw.multiline_text(
        (x - 3, y - 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text(
        (x + 3, y - 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text(
        (x - 3, y + 3), text, font=font, fill=border_color, spacing=spacing)
    draw.multiline_text(
        (x + 3, y + 3), text, font=font, fill=border_color, spacing=spacing)


def _fit_text_to_image(image, text_top, text_bottom, draw, font):
    """Pipes the processes to measure, shrink and wrap text so that it fits within image."""
    image_w, image_h = _measure_image(image)
    top_text_fitted, top_font = _shrink_and_wrap_text(draw, text_top, image_w, image_h, font)
    bottom_text_fitted, bottom_font = _shrink_and_wrap_text(draw, text_bottom, image_w, image_h, font)
    return top_text_fitted, bottom_text_fitted, top_font, bottom_font


def _shrink_and_wrap_text(draw, text, image_w, image_h, normal_font):
    """Tests the text width and applies alterations to make it fit into the image. First shrinking it, then wrapping,
    then shrinking and wrapping."""
    text_w, text_h = _measure_text(draw, text, normal_font, SPACING)
    needs_shrinking = _find_if_needs_fitting(text_w, text_h, image_w, image_h)
    if needs_shrinking is True:
        updated_font = ImageFont.truetype('impact.ttf', 33)
        text_w, text_h = _measure_text(draw, text, normal_font, SPACING)
        needs_wrapping = _find_if_needs_fitting(text_w, text_h, image_w, image_h)
        if needs_wrapping is True:
            wrapped_text = _wrap_text(draw, text, normal_font, image_w)
            new_text_w, new_text_h = _measure_text(draw, wrapped_text, normal_font, SPACING)
            needs_shrinking = _find_if_needs_fitting(new_text_w, new_text_h, image_w, image_h)
            if needs_shrinking is True:
                wrapped_text = _wrap_text(draw, text, updated_font, image_w)
                final_font = updated_font
            else:
                final_font = normal_font
        else:
            wrapped_text = text
            final_font = updated_font
    else:
        wrapped_text = text
        final_font = normal_font
    return wrapped_text, final_font


def _find_if_needs_fitting(text_w, text_h, image_w, image_h):
    """Determines whether the text is too large, returns bool value True if it is.

    >>> _find_if_needs_fitting(110, 5, 100, 100)
    True
    >>> _find_if_needs_fitting(50, 40, 100, 100)
    True
    >>> _find_if_needs_fitting(20, 5, 100, 100)
    False
    """
    if text_w > image_w or text_h > image_h // 4:
        needs_fitting = True
    else:
        needs_fitting = False
    return needs_fitting


def _wrap_text(draw, text, font, image_w):
    """Wraps text around image width, joins it with new line characters."""
    wrapped_text = _intelli_draw(draw, text, font, image_w, SPACING)
    return '\n'.join(wrapped_text)


def _intelli_draw(drawer, text, font, image_w, spacing):
    """Wraps text based measuring against the width of the image

    >>> image = _import_image('test_image.jpg')
    >>> _intelli_draw(ImageDraw.Draw(image), 'Sample text that should be wider than the width of this image', ImageFont\
    .truetype('impact.ttf', 50), 360, 5)
    ['Sample text that', 'should be wider', 'than the width of', 'this image']

    Sourced from Caleb Hattingh, at https://mail.python.org/pipermail/image-sig/2004-December/003064.html
    """
    container_width = image_w - spacing
    words = text.split()
    lines = [words]
    finished = False
    line = 0
    while not finished:
        this_text = lines[line]
        newline = []
        inner_finished = False
        while not inner_finished:
            if drawer.textsize(' '.join(this_text), font)[0] > container_width:
                newline.insert(0, this_text.pop(-1))
            else:
                inner_finished = True
        if len(newline) > 0:
            lines.append(newline)
            line += 1
        else:
            finished = True
    tmp = []
    for i in lines:
        tmp.append(' '.join(i))
    lines = tmp
    return lines
