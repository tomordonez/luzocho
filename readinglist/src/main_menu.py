class MainMenu:
    def __init__(self):
        self.text = None
        self.menu_option = None

    def capture_menu_option_input(self, text):
        self.text = text
        return input(self.text)

    def display_main_menu(self, number_of_saved_books):

        print("\nWelcome to Reading List")
        print("1. Enter a search query")
        print(f"2. View Reading List ({number_of_saved_books} books saved)")
        print("3. Exit\n")

        while True:
            menu_option = self.capture_menu_option_input("Enter a menu option: ")

            if menu_option.isnumeric():
                menu_option_int = int(menu_option)
                if menu_option_int in range(1, 4):
                    break
                else:
                    print("Enter a correct number")
            else:
                print("Enter a correct number")

        return menu_option_int
