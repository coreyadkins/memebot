""" Project initialization script """

from mgapi.handler import MemeGeneratorApiHandler
from vote.vote import MemeVote
import os
import requests
from operator import itemgetter

INPUT_DIR = 'input/'


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

        if task == 'c':
            initialize_corpus()
            task = input('Clear output directory [y/n]?')
            if task == 'y':
                initialize_output()
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
        deobfuscate([' q', ' rrfn ', 'l '])
    )
    top_instances = []
    top_generators = {}
    for instance in builder.get_popular_memes(entries, days=7):
        top_instances.append(instance)

        print('ID: {} is {}'.format(instance['instanceID'], instance['urlName']))
        if instance['generatorID'] not in top_generators.keys():
            top_generators[instance['generatorID']] = builder.get_generator_detail(
                instance['generatorID'],
                instance['urlName']
            )

    save_corpus(top_instances, INPUT_DIR + 'corpus.txt')
    save_generators(
        cull_generators(top_generators),
        INPUT_DIR,
        prune=True
    )


def save_corpus(meme_list, path):
    """ writes list of memes to the specified path """
    with open(path, 'w') as file_handle:
        for meme in meme_list:
            lines = [x.strip() for x in meme['text'] if validate_meme_text(x)]
            file_handle.write('\n'.join(lines))
            file_handle.write('\n')


def save_generators(generators, path, prune=False):
    """ Saves necessary generators, deletes unnecessary """
    existing_names = [file[:-4] for file in os.listdir(path)
                      if file.endswith('.jpg')]
    preserve = []
    for keep in generators:
        preserve.append(keep['urlName'])

        if keep['urlName'] not in existing_names:
            # download
            rq = requests.get(keep['imageUrl'])
            print('Downloading {} from {}'.format(keep['urlName'], keep[
                'imageUrl']))
            with open(path + keep['urlName'] + '.jpg', 'wb') as file:
                file.write(rq.content)
        else:
            print('FOUND: ' + keep['urlName'])

    for kill in [path + file + '.jpg' for file in existing_names
                 if file not in preserve]:
        print('Delete{}: {}'.format(' (not really)'
                                    if not prune else '', kill))
        if prune:
            os.unlink(kill)


def validate_meme_text(text):
    """ NO RUSSIAN, GREEK, ETC.

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


def cull_generators(generators):
    """ Cull generators to the most popular """
    cull_index = max(len(generators) // 8, 4)
    cull_gens = sorted(
        [
            {'urlName': val['urlName'], 'imageUrl': val['imageUrl'], 'ranking': val['ranking']}
            for key, val in generators.items()
        ],
        key=itemgetter('ranking')
    )[:cull_index]

    return cull_gens

if __name__ == '__main__':
    print(main())
