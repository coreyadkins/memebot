""" Builds the corpus for Markov chains """


from mgapi.handler import MemeGeneratorApiHandler
import os
import requests


def main():
    """ main """
    INPUT_DIR = 'input/'

    # username = input('dankm')
    username = '{}{}{}{}{}{}{}'.format(' da', 'nk', 'ma', 'st', 'er', '42', '0 ').strip()
    builder = MemeGeneratorApiHandler(username, 'pdxc0d3gu!ld')
    top_meme_ids = builder.get_popular_meme_ids(500)
    top_memes = [builder.get_meme_detail(x) for x in top_meme_ids]

    top_gen_ids = set([(meme['generatorID'], meme['urlName']) for meme in top_memes])
    top_gens = [builder.get_generator_detail(id, name) for id, name in top_gen_ids]

    write_corpus(top_memes, INPUT_DIR + 'corpus.txt')
    save_generators(top_gens, INPUT_DIR, prune=True)


def write_corpus(meme_list, path):
    """ writes list of memes to the specified path """
    with open(path, 'w') as file_handle:
        for meme in meme_list:
            text = [meme[key] for key in meme if 'text' in key and meme[key] is not None]
            file_handle.write('\n'.join(text).strip() + '\n')


def save_generators(generators, path, prune=False):
    """ Saves necessary generators, deletes unnecessary """
    existing_names = [file[:-4] for file in os.listdir(path) if file.endswith('.jpg')]
    preserve = []

    for keep in generators:
        preserve.append(keep['urlName'])

        if keep['urlName'] not in existing_names:
            # download
            rq = requests.get(keep['imageUrl'])
            print('Downloading {} from {}'.format(keep['urlName'], keep['imageUrl']))
            with open(path + keep['urlName'] + '.jpg', 'wb') as file:
                file.write(rq.content)
        else:
            print('FOUND: ' + keep['urlName'])

    for kill in [path + file + '.jpg' for file in existing_names if file not in preserve]:
        print('Delete{}: {}'.format(' (not really)' if not prune else '', kill))
        if prune:
            os.unlink(kill)


if __name__ == '__main__':
    print(main())
