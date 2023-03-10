class BookSaver:
    def __init__(self):
        self.five_books = None
        self.result_selected = None

    def save_book(self, result_selected, five_books):
        self.result_selected = result_selected
        self.five_books = five_books

        selected_book = []
        match self.result_selected:
            case 1:
                author = self.five_books['book0'][0][0][0]
                title = self.five_books['book0'][0][1]
                publisher = self.five_books['book0'][0][2]
            case 2:
                author = self.five_books['book1'][0][0][0]
                title = self.five_books['book1'][0][1]
                publisher = self.five_books['book1'][0][2]
            case 3:
                author = self.five_books['book2'][0][0][0]
                title = self.five_books['book2'][0][1]
                publisher = self.five_books['book2'][0][2]
            case 4:
                author = self.five_books['book3'][0][0][0]
                title = self.five_books['book3'][0][1]
                publisher = self.five_books['book3'][0][2]
            case 5:
                author = self.five_books['book4'][0][0][0]
                title = self.five_books['book4'][0][1]
                publisher = self.five_books['book4'][0][2]

        selected_book.extend([author, title, publisher])
        print("\n**** Book Saved to Reading List ****")
        print(f"Author: {selected_book[0]}. Title: {selected_book[1]}. Publisher: {selected_book[2]}\n")
        return selected_book
