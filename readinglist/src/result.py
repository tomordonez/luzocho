from collections import defaultdict


class Result:
    
    def __init__(self):
        self.data = None

    def results_menu(self, data):
        self.data = data
        results = defaultdict(list)

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

            results['book' + str(book)].append([author, title, publisher])

        print(f"1. Author: {results['book0'][0][0][0]}. Title: {results['book0'][0][1]}. "
              f"Publisher: {results['book0'][0][2]}")
        print(f"2. Author: {results['book1'][0][0][0]}. Title: {results['book1'][0][1]}. "
              f"Publisher: {results['book1'][0][2]}")
        print(f"3. Author: {results['book2'][0][0][0]}. Title: {results['book2'][0][1]}. "
              f"Publisher: {results['book2'][0][2]}")
        print(f"4. Author: {results['book3'][0][0][0]}. Title: {results['book3'][0][1]}. "
              f"Publisher: {results['book3'][0][2]}")
        print(f"5. Author: {results['book4'][0][0][0]}. Title: {results['book4'][0][1]}. "
              f"Publisher: {results['book4'][0][2]}")
