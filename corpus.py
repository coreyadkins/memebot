""" Builds the corpus for Markov chains """


from mgapi.handler import MemeGeneratorApiHandler


def main():
    """ main """
    username = input('dankm')
    username = 'dankm' + username + 'ter420'

    builder = MemeGeneratorApiHandler(username, 'pdxc0d3gu!ld')
    top_ids = builder.get_popular_meme_ids(500)
    top_memes = [builder.get_meme_detail(x) for x in top_ids]

    write_corpus(top_memes, 'data/mgapi.txt')


def write_corpus(meme_list, path):
    """ writes list of memes to the specified path """
    with open(path, 'w') as file_handle:
        for meme in meme_list:
            text = [meme[key] for key in meme if 'text' in key and meme[key] is not None]
            file_handle.write(' '.join(text).strip() + '\n')


if __name__ == '__main__':
    print(main())
