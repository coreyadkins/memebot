""" Corpus Fetcher

 Loads corpus data from MemeGenerator.net API
 """

import requests
import json


class MemeGeneratorApiHandler:
    """ Fetches mgapi data via API """
    def __init__(self, username, password):
        """ initializes l/p """

        self._username = username
        self._password = password

    def _load_action(self, action, params={}):
        """ Wrapper for API requests """
        url_str = 'http://{}/{}'.format('version1.api.memegenerator.net', action)
        url_params = {} if len(params) == 0 else params
        rq = requests.get(url_str, url_params)
        data_text = rq.text

        try:
            data_json = json.loads(data_text)['result']
        except KeyError:
            raise ValueError('Invalid data at ' + rq.url)

        return data_json

    def _add_login_to_params(self, addl_params=None):
        params = {} if addl_params is None else addl_params
        params.update({'username': self._username, 'password': self._password})
        return params

    def get_popular_meme_ids(self, total, days=None):
        """ Returns list of popular generators

        :return list(int: generator_id)
        """
        top_maymays = []
        max_results = 24

        for i in range(0, total, max_results):
            params = self._add_login_to_params({
                'pageIndex': i // max_results,
                'pageSize': min(max_results, total - i)
            })

            if days is not None:
                params['days'] = days

            data_json = self._load_action('Instances_Select_ByPopular', params)
            top_maymays += [int(meme['instanceID']) for meme in data_json]

        return top_maymays

    def get_trending_meme_ids(self):
        """ Returns list of trending generators

        :return list(int: generator_id)
        """
        # TODO: implement?
        pass
        # data_json = self._load_action('Generators_Select_ByTrending')
        # trending_maymays = self._get_ids_from_json(data_json)
        # return trending_maymays

    def get_meme_detail(self, meme_id):
        """ Get details of meme instanceID

        :return JSON: detail
        """
        params = self._add_login_to_params({'instanceID': meme_id})
        maymay_detail = self._load_action('Instance_Select', params)

        # that's a nice maymay.
        # [(8)D
        return maymay_detail

    def get_generator_detail(self, generator_id, generator_name):
        """ Get generator detail for meme """
        params = self._add_login_to_params({
            'generatorID': generator_id,
            'urlName': generator_name,
        })
        detail = self._load_action('Generator_Select_ByUrlNameOrGeneratorID', params)
        return detail
