""" Voting model """

import sqlite3
import os.path

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
        >>> v.get_votes()
        ('foo', 'bar', 'bar')
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
