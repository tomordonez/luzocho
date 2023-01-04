class Bookshelf:
    def __init__(self):
        self.saved_books = None

    def show_shelf(self, saved_books):
        self.saved_books = saved_books
        if len(self.saved_books) == 0:
            print("\nThere are no saved books\n")
        else:
            print("\n**** Saved Reading List ****\n")
            for book in self.saved_books:
                print(f"Author: {book[0]}. Title: {book[1]}. Publisher: {book[2]}")
