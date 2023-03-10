from pathlib import Path


class BookshelfExporter:
    @staticmethod
    def export_bookshelf_textfile(saved_books):
        number_of_saved_books = len(saved_books)

        if number_of_saved_books == 0:
            print(f"Your Reading List was not exported. You saved {number_of_saved_books} books.")

        elif number_of_saved_books > 0:
            print(f"Your Reading List was exported with {number_of_saved_books} book(s).")

            filepath = Path(__file__).parent.parent / 'data' / 'bookshelf_data.txt'
            with filepath.open('w+') as bookshelf_data:
                if saved_books is not None:
                    for book in saved_books:
                        bookshelf_data.write(str(book) + "\n")
