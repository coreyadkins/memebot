"""Generates a random gender and gender descriptor."""
import random

def generate_text():
    """Generates random text."""
    descriptor = 'Androgynous Anti Butch Chibi Celestial Cisgender Crypto Dandy \
    Dysphoric Demi Drag Eggy Fake Femme Fiendish Flirtacious Genderfluid Genderpunk \
    Genderqueer Glass Hard High Lathargic Lipstick Low Manicured Moon Nonbinary \
    Nonconforming Questioning Secure Soft Sparkle Spooky Sporty Sun Transfemmenine \
    Transgender Transmasculine Trash Witchy'.split()

    gender= 'Agender Abimegender Absorgender Androgyne Bear Bigender Boy Dameon \
    Eater Gem Genderqueer Ghost Girl God Goddess Goth Hologram Man Neutrois \
    Otherkin Pangender Screaming Skeleton Twink Trash Woman'.split()

    return ('This is a meme about a {} {}'.format(random.choice(descriptor), random.choice(gender)))
