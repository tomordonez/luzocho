import urllib.request
import json
import string


class Search:
    def __init__(self):
        self.query = None
        self.url = None

    def search_query(self, query):
        self.query = query.translate(str.maketrans('', '', string.punctuation)) \
            .lower() \
            .replace(" ", "+")

        google_books_base_url = "https://www.googleapis.com/books/v1/volumes?q="

        url = google_books_base_url + self.query
        return url

    def request_data(self, url):
        self.url = urllib.request.urlopen(url)
        data = self.url.read()
        json_data = json.loads(data.decode('utf-8'))
        return json_data
