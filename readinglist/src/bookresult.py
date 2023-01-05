from collections import defaultdict


class BookResult:
    def __init__(self):
        self.data = None

    def get_five_book_results(self, data):
        self.data = data
        five_books = defaultdict(list)

        for book in range(5):

            try:
                author = self.data['items'][book]['volumeInfo']['authors']
            except:
                author = "Not found"

            try:
                title = self.data['items'][book]['volumeInfo']['title']
            except:
                title = "Not found"

            try:
                publisher = self.data['items'][book]['volumeInfo']['publisher']
            except:
                publisher = "Not found"

            five_books['book' + str(book)].append([author, title, publisher])

        return five_books
