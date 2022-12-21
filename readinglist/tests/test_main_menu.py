from unittest import TestCase
from unittest.mock import patch

from readinglist.src.main_menu import MainMenu


class MenuTestCase(TestCase):
    def setUp(self):
        self.menu = MainMenu()

    def test_main_menu_loads(self):
        self.assertIsInstance(self.menu, MainMenu)

    @patch('builtins.input', return_value="1")
    def test_validate_search_menu_option_when_passing_1(self, mock_input):
        validated_option = self.menu.validate_menu_option()
        self.assertEqual(validated_option, 1)

    @patch('builtins.input', return_value="2")
    def test_validate_reading_list_menu_option_when_passing_2(self, mock_input):
        validated_option = self.menu.validate_menu_option()
        self.assertEqual(validated_option, 2)

    @patch('builtins.input', return_value="3")
    def test_validate_reading_list_menu_option_when_passing_3(self, mock_input):
        validated_option = self.menu.validate_menu_option()
        self.assertEqual(validated_option, 3)