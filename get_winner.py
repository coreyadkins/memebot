"""Takes in a dictionary of votes, and returns the meme with the highest wins to contests."""


from vote.vote import MemeVote


def group_by(iterable, key):
    """Place each item in an iterable into a bucket based on calling the key
    function on the item."""
    group_to_items = {}
    for item in iterable:
        group = key(item)
        if group not in group_to_items:
            group_to_items[group] = []
        group_to_items[group].append(item)
    return group_to_items


def get_winner_meme(vote):
    """Simple key for groupby function in get_meme_to_wins function."""
    return vote['winner']


def get_memes_to_wins(memes_to_votes):
    memes_to_wins = {
        meme: [len(votes)]
        for meme, votes
        in memes_to_votes
        }
    return memes_to_wins


def get_memes_to_contests(memes_to_votes):
    memes_to_contests = {
        meme: [votes['meme1'] if meme == votes['meme1'] else votes['meme2']]
        for meme, votes
        in memes_to_votes
        }
    return memes_to_contests



def get_meme_to_wins(contests_to_winners):
    """Takes in a dictionary of complete votes and returns an array of meme to the number of wins they have"""
    meme_to_votes = group_by(contests_to_winners, get_winner_meme)
    memes_to_wins = get_meme_to_wins(meme_to_votes)
    memes_to_contests = get_memes_to_contests(meme_to_votes)
    memes_to



    return





def get_winner():
    contests_to_winners = MemeVote().get_votes()
    meme_to_wins = get_meme_to_wins(contests_to_winners)