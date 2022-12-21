from unittest import TestCase
from unittest.mock import Mock, patch
from readinglist.src.search import Search


class TestSearch(TestCase):

    @patch('readinglist.src.search.urllib.request.urlopen')
    def test_request_response(self, mock_urlopen):
        mock_urlopen.return_value.status = 200
        url_query = Search().construct_search_query_url('TDD in Python')
        response = Search().request_response_google_api(url_query)
        self.assertIsNotNone(response)

