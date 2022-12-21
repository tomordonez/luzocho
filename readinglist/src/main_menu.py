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
            return "Search query"
        elif menu_option == "2":
            return "Reading list"
        elif menu_option == "3":
            return "Exit"
        else:
            print("You entered an incorrect option")
            return "Incorrect option"

    def main_menu(self):

        print("Welcome to Reading List")
        print("1. Enter a search query")
        print("2. View Reading List")
        print("3. Exit")

        menu_option = self.validate_menu_option()
        self.set_menu_option(menu_option)
