class ResultMenu:

    def __init__(self):
        self.results = None

    def display_results_menu(self, five_books):
        self.results = five_books

        print(f"1. Author: {self.results['book0'][0][0][0]}. Title: {self.results['book0'][0][1]}. "
              f"Publisher: {self.results['book0'][0][2]}")
        print(f"2. Author: {self.results['book1'][0][0][0]}. Title: {self.results['book1'][0][1]}. "
              f"Publisher: {self.results['book1'][0][2]}")
        print(f"3. Author: {self.results['book2'][0][0][0]}. Title: {self.results['book2'][0][1]}. "
              f"Publisher: {self.results['book2'][0][2]}")
        print(f"4. Author: {self.results['book3'][0][0][0]}. Title: {self.results['book3'][0][1]}. "
              f"Publisher: {self.results['book3'][0][2]}")
        print(f"5. Author: {self.results['book4'][0][0][0]}. Title: {self.results['book4'][0][1]}. "
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
