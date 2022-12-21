import sys

from readinglist.src.main_menu import MainMenu
from readinglist.src.search import Search
from readinglist.src.result import Result
from readinglist.src.bookshelf import Bookshelf


def run():
    saved_books = []

    while True:
        menu_option = MainMenu().main_menu()

        if menu_option == 1:
            search = Search()
            query = input("Enter the search query: ")
            url = search.search_query(query)
            data = search.request_data(url)
            result = Result()
            five_books = result.get_five_book_results(data)
            result.display_results_menu(five_books)
            result_selected = result.prompt_result_option()
            open_bookshelf = Bookshelf()
            selected_book = open_bookshelf.save_book(result_selected, five_books)
            saved_books.append(selected_book)

        elif menu_option == 2:
            open_bookshelf = Bookshelf()
            open_bookshelf.show_shelf(saved_books)

        elif menu_option == 3:
            break
