from Movie_menu_items import Movie_Menu_Items

#--------------------------------DEFINES FUNCTIONS THAT ARE ACCESSED FROM MAIN MENU----------------------------------------------#
class Movie_Menu:
    def __init__(self, movie_menu_items):
        self.movie_menu_items = movie_menu_items
    
    def print_movie_menu(self):
        print("Welcome to our Movie Database. These are our options: ")
        for item in self.movie_menu_items:
            item.show_item()
            
        
    def add_movie(self, name, rating):
        new_item = Movie_Menu_Items(name, rating)
        self.movie_menu_items.append(new_item)

    def delete_movie(self, name):
        for item in self.movie_menu_items:
            if item.name == name:
                self.movie_menu_items.remove(item)
                return print(f"{name} was removed from our database!")
        return print(f"{name} was not in the list!")

    def edit_movie_rating(self, name):
        for item in self.movie_menu_items:
            if item.name == name:
                rating = float(input(f"What is the updated rating of {name}?: "))
                item.rating = rating
                return print(f"{name}'s rating was updated!")
        return print(f"{name} is not in our database!")

        #print, add, delete, update
        #add, delete edit , take order,

#-----------------------------------------------------------END-----------------------------------------------------------------#