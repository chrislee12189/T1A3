class Movie_Menu_Items:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def show_item(self):
        print(f"{self.name}: Rating: {self.rating}")