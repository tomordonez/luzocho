from pathlib import Path
import ast


class BookshelfImporter:

    @staticmethod
    def import_bookshelf_textfile():
        filepath = Path(__file__).parent.parent / 'data' / 'bookshelf_data.txt'
        saved_books = []
        if filepath.exists():
            with filepath.open('r') as file:
                file_data = file.readlines()

            for element in file_data:
                saved_books.append(ast.literal_eval(element))
            return saved_books
        else:
            return saved_books
