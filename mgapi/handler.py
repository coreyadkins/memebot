""" Corpus Fetcher

 Loads corpus data from MemeGenerator.net API
 """

import urllib.request
import json


class MemeGeneratorApiHandler:
    """ Fetches mgapi data via API """
    def __init__(self, username, password):
        """ initializes l/p """

        self._username = username
        self._password = password

    def _get_request_url(self, action, params=''):
        """ String builder for API endpoints """
        url = 'http://{}/{}'.format(
            'version1.api.memegenerator.net',
            action
        )

        for i, param in enumerate(params):
            url = self._add_url_param(url, param, params[param])

        return url

    def _add_url_param(self, url, name, val):
        """ adds a parameter to the URL string """
        delim = '&' if '?' in url else '?'
        param = '{}{}={}'.format(delim, name, val)
        return url + param

    def _load_url_as_json(self, url):
        """ Loads a URL, returns JSON data as an object

        :return json_data
        """
        with urllib.request.urlopen(url) as text:
            data_str = '\n'.join([line.decode('UTF-8') for line in text])

        data_json = json.loads(data_str)
        return data_json['result']

    def _get_ids_from_json(self, meme_list):
        """ Parse out just the IDs from a list of memes

        :return list(int: generator_id)
        """
        ids = [int(maymay['instanceID']) for maymay in meme_list]
        return ids

    def get_popular_meme_ids(self, total, days=None):
        """ Returns list of popular generators

        :return list(int: generator_id)
        """
        top_maymays = []
        max_results = 24
        for i in range(0, total, max_results):
            fetch_url = self._get_request_url(
                'Instances_Select_ByPopular',
                {
                    'pageIndex': i // max_results,
                    'pageSize': min(max_results, total - i),
                    'username': self._username,
                    'password': self._password
                }
            )

            if days is not None:
                fetch_url = self._add_url_param(fetch_url, {'days': days})

            url_data = self._load_url_as_json(fetch_url)
            top_maymays += self._get_ids_from_json(url_data)

        return top_maymays

    def get_trending_meme_ids(self):
        """ Returns list of trending generators

        :return list(int: generator_id)
        """
        fetch_url = self._get_request_url('Generators_Select_ByTrending')
        url_data = self._load_url_as_json(fetch_url)
        trending_maymays = self._get_ids_from_json(url_data)
        return trending_maymays

    def get_meme_detail(self, meme_id):
        """ Get details of meme of generatorID: meme_id

        :return JSON: detail
        """
        fetch_url = self._get_request_url(
            'Instance_Select',
            {
                'username': self._username,
                'password': self._password,
                'instanceID': meme_id
            }
        )

        maymay_detail = self._load_url_as_json(fetch_url)

        # that's a nice maymay.
        # [(8)D
        return maymay_detail
