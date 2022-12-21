import urllib.request
import json
import string

from readinglist.src.constants import BASE_URL


class Search:
    def __init__(self):
        self.query = None
        self.url = None

    def construct_search_query_url(self, query):
        self.query = query.translate(str.maketrans('', '', string.punctuation)) \
            .lower() \
            .replace(" ", "+")

        url = BASE_URL + self.query
        return url

    def request_response_google_api(self, url):
        self.url = urllib.request.urlopen(url)
        if self.url.status == 200:
            return self.url
        else:
            return None

    def construct_json_data_google_api(self, url):
        self.url = urllib.request.urlopen(url)
        data = self.url.read()
        json_data = json.loads(data.decode('utf-8'))
        return json_data
