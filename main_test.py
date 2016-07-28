from image_writer import write_text_to_image


def main():
    """Simulating program being called by outside."""
    write_text_to_image('NOT SURE IF SINCERE', 'OR JUST SARCASM', 'futurama_fry.jpg')


if __name__ == '__main__':
    main()