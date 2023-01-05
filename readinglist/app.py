from bookshelf_exporter import BookshelfExporter
from bookshelf_importer import BookshelfImporter
from main_menu_option import MainMenuOption
from readinglist.src.main_menu import MainMenu


def run():
    saved_books = BookshelfImporter().import_bookshelf_textfile()

    while True:
        number_of_saved_books = len(saved_books)
        menu_option = MainMenu().display_main_menu(number_of_saved_books)

        if menu_option == 1:
            selected_book = MainMenuOption().enter_search_query()
            if selected_book is not None:
                saved_books.append(selected_book)

        elif menu_option == 2:
            MainMenuOption().view_reading_list(saved_books)

        elif menu_option == 3:
            BookshelfExporter().export_bookshelf_textfile(saved_books)
            break
