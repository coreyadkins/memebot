""" Voting model """

import sqlite3
import os.path
from operator import itemgetter
# from itertools import groupby

class MemeVote:
    """ Wrapper for various voting DB functionality """
    DB_PATH = 'db.sqlite3'

    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def _get_db_path(self):
        """ Get the path to the database """
        path = self.DB_PATH
        if self.test_mode:
            path += '.test'

        return path

    def vote(self, meme1, meme2, winner):
        """ Adds the two entrants and winner into the table

        >>> v = MemeVote(test_mode=True)
        >>> v.create_schema()
        >>> v.vote('foo', 'bar', 'foo')
        >>> v._raw_query('SELECT winner FROM votes LIMIT 1')
        [('foo',)]
        """
        with sqlite3.connect(self._get_db_path()) as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO votes (meme1, meme2, winner) VALUES (?, ?, ?)',
                (meme1, meme2, winner)
            )
            connection.commit()

    def get_votes(self):
        """ Get all votes, no SQL processing except orderby winner

        >>> v = MemeVote(test_mode=True)
        >>> v.create_schema()
        >>> v.vote('foo', 'bar', 'bar')
        >>> v.get_votes()[0]['meme1'] + v.get_votes()[0]['winner']
        'foobar'
        """
        votes = []
        with sqlite3.connect(self._get_db_path()) as connection:
            cursor = connection.cursor()

            try:
                cursor.execute('SELECT meme1, meme2, winner FROM votes ORDER BY winner')
            except sqlite3.Error:
                raise FileNotFoundError('Database not initialized')

            for maymay in cursor.fetchall():
                votes.append({'meme1': maymay[0], 'meme2': maymay[1], 'winner': maymay[2]})

        return votes

    def get_least_voted(self, items, num=2):
        """ Select (num) number of the least-voted instances

        >>> v = MemeVote(test_mode=True)
        >>> v.vote('alpha', 'beta', 'alpha')
        >>> v.vote('beta', 'gamma', 'gamma')
        >>> v.vote('gamma', 'delta', 'gamma')
        >>> v.vote('alpha', 'gamma', 'alpha')
        >>> v.get_least_voted(['alpha', 'beta', 'gamma', 'delta', 'omega'])
        ['omega', 'delta']
        """
        searches = [vote['meme1'] + '|' + vote['meme2'] for vote in self.get_votes()]
        tally = {}
        for item in items:
            tally[item] = len([x for x in searches if item in x])

        least = [t[0] for t in sorted(tally.items(), key=itemgetter(1))[:num]]
        return least

    def _raw_query(self, query):
        """ Execute a raw query

        >>> v = MemeVote(test_mode=True)
        >>> v.create_schema()
        >>> v._raw_query("SELECT name FROM sqlite_master WHERE type='table'")
        [('votes',)]
        """
        with sqlite3.connect(self._get_db_path()) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def create_schema(self):
        """ Create the database schema

        >>> v = MemeVote(test_mode=True)
        >>> v.create_schema()
        >>> os.path.isfile(v._get_db_path())
        True
        >>> v = MemeVote(test_mode=True)
        >>> v.create_schema()
        >>> v._raw_query('SELECT * from votes')
        []
        """
        with sqlite3.connect(self._get_db_path()) as connection:
            cursor = connection.cursor()
            cursor.execute('DROP TABLE IF EXISTS votes')
            cursor.execute('CREATE TABLE votes(meme1 TEXT, meme2 TEXT, winner TEXT)')

            connection.commit()

