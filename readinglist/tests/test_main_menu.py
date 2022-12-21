from unittest import TestCase
from unittest.mock import patch

from readinglist.src.main_menu import MainMenu
from readinglist.src.search import Search


class MenuTestCase(TestCase):
    def setUp(self):
        self.menu = MainMenu()
        self.search_menu = Search()

    def test_main_menu_loads(self):
        self.assertIsInstance(self.menu, MainMenu)

    @patch('builtins.input', return_value=1)
    def test_validate_search_menu_option_when_passing_one(self, mock_input):
        validated_option = self.menu.validate_menu_option()
        self.assertEqual(validated_option, "Search query")
