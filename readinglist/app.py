from readinglist.src.main_menu import MainMenu
from readinglist.src.search import Search
from readinglist.src.result import Result
from readinglist.src.bookshelf import Bookshelf


def run():
    saved_books = []

    while True:
        menu_option = MainMenu().display_main_menu()

        if menu_option == 1:
            search = Search()
            query = input("Enter the search query: ")
            url = search.construct_search_query_url(query)
            data = search.construct_json_data_google_api(url)

            if data is not None:
                result = Result()
                if data['totalItems'] is 0:
                    print("\n**** No results were found ****")
                else:
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
