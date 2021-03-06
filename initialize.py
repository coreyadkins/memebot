""" Project initialization script """

from mgapi.handler import MemeGeneratorApiHandler
from vote.vote import MemeVote
import os
import requests
from operator import itemgetter
from text_generator import generate_text
from image_writer import write_text_to_image
from randomfile import get_random_input_file, get_random_output_path

INPUT_DIR = 'input/'
MAX_INSTANCES = 100
MAX_GENERATORS = 15


def main():
    """ main """
    task = ''
    while task != 'q':
        print(' SELECT TASK '.center(40, '='))
        print('PROCEED WITH CAUTION, THIS CAN DELETE AND OVERWRITE DATA')
        task = input(
            'Initialize [d]atabase, [c]orpus, [o]utput, or [q]uit? ').lower(
            ).strip()

        if task == 'd':
            initial_d()
        elif task == 'c':
            initialize_corpus()
        elif task == 'o':
            initialize_output()
        else:
            task = 'q'


def initial_d():
    """ Initialize the database """
    vote = MemeVote(7)
    vote.create_schema()
    print('Database created')
    print('')


def initialize_corpus():
    """ Gets  number of dank memes to use for the corpus files, creates files"""
    num_entries = input('Number of entries to use (blank to quit): ')
    if num_entries.isnumeric():
        num_entries = abs(int(num_entries))
        build_corpus(num_entries)


def initialize_output():
    """ Create/clear the output directory """
    OUT_DIR = 'output'
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    junk = [x for x in os.listdir(OUT_DIR) if x[-4:] == '.jpg']
    for file in junk:
        os.unlink(OUT_DIR + '/' + file)

    print('Output directory initialized.')
    print('')
    for i in range(MAX_INSTANCES):
        top_line, bottom_line = generate_text()
        image_name = get_random_input_file()
        image = write_text_to_image(top_line, bottom_line, image_name)
        print('Writing to {}:'.format(image_name))
        print('\t{}'.format(top_line))
        print('\t{}'.format(bottom_line))
        save_image(image, image_name)


def deobfuscate(chars):
    """ Deobfuscate creds

    >>> deobfuscate(['hg ', ' fe ', 'dc ', 'ba '])
    'abcdefgh'
    """
    chars.reverse()
    return ''.join([x[::-1].strip() for x in chars])


def build_corpus(entries):
    """ Build a corpus from the dankest memes and download the top generators """
    builder = MemeGeneratorApiHandler(
        deobfuscate([' 02 ', ' 4r ', 'etsa', ' mk', ' nad ']),
        deobfuscate([' q', ' rrfn ', 'l ']))
    top_instances = []
    top_generators = {}
    for instance in builder.get_popular_memes(entries, days=7):
        top_instances.append(instance)

        print('ID: {} is {}'.format(
            instance['instanceID'],
            instance['urlName']
        ))

        if instance['generatorID'] not in top_generators.keys():
            top_generators[instance[
                'generatorID']] = builder.get_generator_detail(
                    instance['generatorID'], instance['urlName'])

    save_corpus(top_instances, INPUT_DIR + 'corpus.txt')
    save_generators(cull_generators(top_generators, MAX_GENERATORS), INPUT_DIR, prune=True)
    print('')


def save_corpus(meme_list, path):
    """ writes list of memes to the specified path """
    with open(path, 'w') as file_handle:
        for meme in meme_list:
            lines = [x.strip() for x in meme['text'] if validate_meme_text(x)]
            file_handle.write('\n'.join(lines))
            file_handle.write('\n')


def save_generators(generators, path, prune=False):
    """ Saves necessary generators, deletes unnecessary """
    downloaded_gens = [file[:-4] for file in os.listdir(path)
                       if file.endswith('.jpg')]

    # which files to keep
    gens_to_save = []
    for gen in generators:
        gens_to_save.append(gen['urlName'])

        if gen['urlName'] not in downloaded_gens:
            # download
            rq = requests.get(gen['imageUrl'])
            print('Downloading {} from {}'.format(gen['urlName'], gen[
                'imageUrl']))
            with open(path + gen['urlName'] + '.jpg', 'wb') as file:
                file.write(rq.content)
        else:
            print('FOUND: ' + gen['urlName'])

    # which files to delete
    for kill in [path + file + '.jpg' for file in downloaded_gens
                 if file not in gens_to_save]:
        print('Delete{}: {}'.format(' (not really)'
                                    if not prune else '', kill))
        if prune:
            os.unlink(kill)


def validate_meme_text(text):
    """ Validate text as usable, e.g. Latin characters

    # TODO: maybe more?

    >>> validate_meme_text('Ω')
    False
    >>> validate_meme_text('Alpha and Ω')
    True
    """
    if text is None:
        valid = False
    else:
        alphas = [x for x in text if x.lower() in 'abcdefghijklmnopqrstuvwxyz']
        valid = len(alphas) > 0

    return valid


def cull_generators(generators, max_size):
    """ Cull generators to the most popular, based on ranking

    Doctest 1:
    Returned list should have only 5 items
    Last generator should have ranking: 1, i.e. be first in culled list

    Doctest 2:
    Do not return more generators than available.
    >>> gens = {}
    >>> for i in range(10): gens[i] = {'ranking': 10 - i, 'urlName': 0, 'imageUrl': 0}
    >>> gens = cull_generators(gens, 5)
    >>> len(gens) - gens[0]['ranking']
    4
    >>> gens = {}
    >>> for i in range(10): gens[i] = {'ranking': 10 - i, 'urlName': 0, 'imageUrl': 0}
    >>> len(cull_generators(gens, 15))
    10
    """
    cull_index = min(len(generators), max_size)
    cull_gens = sorted(
        [
            {'urlName': val['urlName'],
             'imageUrl': val['imageUrl'],
             'ranking': val['ranking']} for key, val in generators.items()
        ],
        key=itemgetter('ranking'))

    return cull_gens[:cull_index]


def save_image(image, image_name):
    file_name = str(image_name).replace('input/', '')
    output_name = get_random_output_path(file_name)
    if not os.path.exists('output'):
        os.makedirs('output')
    image.save(output_name)


if __name__ == '__main__':
    print(main())
