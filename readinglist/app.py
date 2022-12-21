import sys

from readinglist.src.main_menu import MainMenu
from readinglist.src.search import Search


def run():
    menu_option = MainMenu().main_menu()
    print(menu_option)

    if menu_option == "1":
        search = Search()
        query = input("Enter the search query: ")
        url = search.search_query(query)
        data = search.request_data(url)

    elif menu_option == "2":
        pass

    elif menu_option == "3":
        sys.exit()
