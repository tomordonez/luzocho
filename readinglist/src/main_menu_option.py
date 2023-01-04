from bookresult import BookResult
from booksaver import BookSaver
from bookshelf import Bookshelf
from resultmenu import ResultMenu
from search import Search


class MainMenuOption:
    @staticmethod
    def enter_search_query():
        search = Search()
        query = input("Enter the search query: ")
        url = search.construct_search_query_url(query)
        data = search.construct_json_data_google_api(url)

        if data is not None:
            result_menu = ResultMenu()
            book_result = BookResult()

            if data['totalItems'] == 0:
                print("\n**** No results were found ****")
            else:
                five_books = book_result.get_five_book_results(data)
                result_menu.display_results_menu(five_books)
                result_selected = result_menu.prompt_result_option()

                book_saver = BookSaver()
                selected_book = book_saver.save_book(result_selected, five_books)
                return selected_book

    @staticmethod
    def view_reading_list(saved_books):
        open_bookshelf = Bookshelf()
        open_bookshelf.show_shelf(saved_books)
