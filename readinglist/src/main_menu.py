from readinglist.src.search import Search


class MainMenu:
    def __init__(self):
        self.text = None
        self.menu_option = None

    def get_menu_option(self):
        return self.menu_option

    def set_menu_option(self, menu_option):
        self.menu_option = menu_option

    def menu_option_input(self, text):
        self.text = text
        return input(self.text)

    def validate_menu_option(self):
        menu_option = self.menu_option_input("Enter a menu option: ")
        if menu_option == "1":
            return 1
        elif menu_option == "2":
            return 2
        elif menu_option == "3":
            return 3
        else:
            return "Incorrect option"

    def main_menu(self):

        print("Welcome to Reading List")
        print("1. Enter a search query")
        print("2. View Reading List")
        print("3. Exit")

        while True:
            menu_option = self.menu_option_input("Enter a menu option: ")

            if menu_option.isnumeric():
                menu_option_int = int(menu_option)
                if menu_option_int in range(1, 4):
                    break
                else:
                    print("Enter a correct number")
            else:
                print("Enter a correct number")

        return menu_option_int
