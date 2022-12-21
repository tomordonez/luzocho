import urllib.request
import json
import string

from readinglist.src.constants import BASE_URL


class Search:
    def __init__(self):
        self.query = None
        self.url = None

    def search_query(self, query):
        self.query = query.translate(str.maketrans('', '', string.punctuation)) \
            .lower() \
            .replace(" ", "+")

        url = BASE_URL + self.query
        return url

    def request_response(self, url):
        self.url = urllib.request.urlopen(url)
        if self.url.status == 200:
            return self.url
        else:
            return None

    def request_data(self, url):
        self.url = urllib.request.urlopen(url)
        data = self.url.read()
        json_data = json.loads(data.decode('utf-8'))
        return json_data
