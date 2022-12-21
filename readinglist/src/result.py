from collections import defaultdict


class Result:

    def __init__(self):
        self.five_books = None
        self.results = None
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

    def display_results_menu(self, five_books):
        self.results = five_books

        print(f"1. Author: {self.results['book0'][0][0][0]}. Title: {five_books['book0'][0][1]}. "
              f"Publisher: {self.results['book0'][0][2]}")
        print(f"2. Author: {self.results['book1'][0][0][0]}. Title: {five_books['book1'][0][1]}. "
              f"Publisher: {self.results['book1'][0][2]}")
        print(f"3. Author: {self.results['book2'][0][0][0]}. Title: {five_books['book2'][0][1]}. "
              f"Publisher: {self.results['book2'][0][2]}")
        print(f"4. Author: {self.results['book3'][0][0][0]}. Title: {five_books['book3'][0][1]}. "
              f"Publisher: {self.results['book3'][0][2]}")
        print(f"5. Author: {self.results['book4'][0][0][0]}. Title: {five_books['book4'][0][1]}. "
              f"Publisher: {self.results['book4'][0][2]}")

    def prompt_result_option(self):

        while True:
            save_option = input("Select the book to save to reading list [1-5]: ")

            if save_option.isnumeric():
                save_option_int = int(save_option)
                if save_option_int in range(1, 6):
                    break
                else:
                    print("Enter a correct number")
            else:
                print("Enter a correct number")

        return save_option_int
