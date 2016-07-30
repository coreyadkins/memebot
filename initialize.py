""" Project initialization script """

from mgapi.handler import MemeGeneratorApiHandler
from vote.vote import MemeVote
import os
import requests

INPUT_DIR = 'input/'


def main():
    """ main """
    task = ''
    while task != 'q':
        print(' SELECT TASK '.center(40, '='))
        print('PROCEED WITH CAUTION, THIS CAN DELETE AND OVERWRITE DATA')
        task = input(
            'Initialize [d]atabase, initialize [c]orpus, or [q]uit? ').lower(
            ).strip()

        if task == 'd':
            initial_d()
        elif task == 'c':
            initialize_corpus()
        else:
            task = 'q'


def initial_d():
    """ Initialize the database """
    vote = MemeVote()
    vote.create_schema()
    print('Database created')
    print('')


def initialize_corpus():
    """ Gets  number of dank memes to use for the corpus files, creates files"""
    num_entries = input('Number of entries to use (blank to quit): ')
    if num_entries.isnumeric():
        num_entries = abs(int(num_entries))
        build_corpus(num_entries)


def build_corpus(entries):
    username = '{}{}{}{}{}{}{}'.format(' da', 'nk', 'ma', 'st', 'er', '42',
                                       '0 ').strip()

    builder = MemeGeneratorApiHandler(username, 'pdxc0d3gu!ld')
    top_instances = []
    top_generators = {}
    for inst in builder.get_popular_meme_ids(entries):
        detail = builder.get_meme_detail(inst)
        top_instances.append(detail)

        print('ID: {} is {}'.format(inst, detail['displayName']))
        if not detail['generatorID'] in top_generators.keys():
            top_generators[detail['generatorID']] = builder.get_generator_detail(
                detail['generatorID'],
                detail['urlName']
            )

    save_corpus(top_instances, INPUT_DIR + 'corpus.txt')
    save_generators(top_generators, INPUT_DIR, prune=True)


def save_corpus(meme_list, path):
    """ writes list of memes to the specified path """
    with open(path, 'w') as file_handle:
        for meme in meme_list:
            text = [meme[key] for key in meme
                    if 'text' in key and meme[key] is not None]
            file_handle.write('\n'.join(text).strip() + '\n')


def save_generators(generators, path, prune=False):
    """ Saves necessary generators, deletes unnecessary """
    existing_names = [file[:-4] for file in os.listdir(path)
                      if file.endswith('.jpg')]
    preserve = []

    for _, keep in generators.items():
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


if __name__ == '__main__':
    print(main())
