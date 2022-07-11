class Movie_Menu_Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_item(self):
        print(f"{self.name}: ${self.price}")