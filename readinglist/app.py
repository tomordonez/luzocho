import sys

from readinglist.src.main_menu import MainMenu
from readinglist.src.search import Search
from readinglist.src.result import Result


def run():
    menu_option = MainMenu().main_menu()

    if menu_option == "1":
        search = Search()
        query = input("Enter the search query: ")
        url = search.search_query(query)
        data = search.request_data(url)
        result = Result()
        five_books = result.get_five_book_results(data)
        result.display_results_menu(five_books)
        result_selected = result.prompt_result_option()

    elif menu_option == "2":
        pass

    elif menu_option == "3":
        sys.exit()
