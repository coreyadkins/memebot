"""Takes in a dictionary of votes, and returns the meme with the highest wins to contests."""

from vote.vote import MemeVote
from collections import defaultdict


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item.
    """
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def get_winner_meme(vote):
    """Simple key for groupby function in get_meme_to_wins function.
    """
    return vote['winner']


def get_memes_to_participated_votes(contests):
    """Takes in all the votes, and process them into two dictionaries, then updates the first dictionary by the second.
    """
    meme_in_contest_as_meme_1 = group_by(contests, get_contest_meme_1)
    meme_in_contest_as_meme_2 = group_by(contests, get_contest_meme_2)
    meme_in_contest_as_meme_1.update(meme_in_contest_as_meme_2)
    return meme_in_contest_as_meme_1


def get_contest_meme_1(vote):
    """Simple key for groupby function in get_meme_to_wins function.
    """
    return vote['meme1']


def get_contest_meme_2(vote):
    """Simple key for groupby function in get_meme_to_wins function.
    """
    return vote['meme2']


def get_memes_to_wins(memes_to_votes):
    """Maps a dictionary of memes to complete votes to a dictionary of memes to the number of wins each has.
    """
    memes_to_wins = {
        meme: len(votes)
        for meme, votes in memes_to_votes.items()
    }
    return memes_to_wins


def get_memes_to_contests(memes_to_participated_votes):
    """Maps a dictionary of memes to complete votes to a dictionary of memes to the number of contests each had.
    """
    memes_to_contests = {
        meme: len(votes)
        for meme, votes in memes_to_participated_votes.items()
    }
    return memes_to_contests


def get_memes_to_numbers(wins, contests):
    """Takes in a dictionary of memes_to_wins and a dictionary of memes_to_contests and returns a dictionary of
     memes to their win-score and their participation score
     """
    memes_to_numbers = defaultdict(list)
    for item in (wins, contests):
        for key, value in item.items():
            memes_to_numbers[key].append(value)
    return memes_to_numbers


def get_memes_to_ratings(memes_to_numbers):
    """Takes in dictionary of to their win-score and their participation score and determins their rating by dividing win
    score by participation score
    """
    memes_to_ratings = {
        meme: (numbers[0] / numbers[1])
        for meme, numbers in memes_to_numbers.items() if len(numbers) == 2
    }
    return memes_to_ratings


def get_overated_meme(ratings):
    """Takes in a dictionary of memes to ratings and returns the meme with the highest rating.
    """
    inverse = [(value, key) for key, value in ratings.items()]
    return max(inverse)[1]


def get_winner_meme():
    """Takes in a dictionary of complete votes and returns an array of meme to the number of wins they have
    """
    contests = MemeVote().get_votes()
    meme_to_won_votes = group_by(contests, get_winner_meme)
    memes_to_wins = get_memes_to_wins(meme_to_won_votes)
    memes_to_participated_votes = get_memes_to_participated_votes(contests)
    memes_to_contests = get_memes_to_contests(memes_to_participated_votes)
    memes_to_numbers = get_memes_to_numbers(memes_to_wins, memes_to_contests)
    memes_to_ratings = get_memes_to_ratings(memes_to_numbers)
    winner_meme = get_overated_meme(memes_to_ratings)
    return (winner_meme)
