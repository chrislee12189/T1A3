from os import system

from pkg_resources import working_set
from Movie_menu_items import Movie_Menu_Items
from Movie_Menu import Movie_Menu
from seed import movie_seed
from rent import Rent

#---------------------------------------TO DO LIST-----------------------------------------#
#   show list = works 
#   add movie = works
#   adjust rating = takes input but doesnt save it/update it
#   delete movie = broken
#   rent movie = takes movie name and copy nums but breaks after that
#   exit = works


movie_menu = movie_seed()
#-----------------------------------------MAIN MENU FOR TERMINAL APP----------------------------------------------------------#
def print_options():
    print("1.Show movie list")
    print("2.Add a movie to our database")
    print("3.Edit the rating of a movie on our database")
    print("4.Delete a movie from our database")
    print("5.Rent a movie from our collection")
    print("6.Exit")
    option = input("Select an option (1-6): ")
    return option
#------------------------------------------END MAIN MENU-----------------------------------------------------------------------#
#------------------------------------------DEFINE MENU OPTIONS-----------------------------------------------------------------#
def add_movie():
    name=input("Whats the name of the movie youre adding?: ")
    price = float(input(f"Whats the rating of {name}?: "))
    movie_menu.add_movie(name, price)

def edit_rating():
    movie_menu.print_movie_menu()
    name = input("Whats the name of the movie who's rating youd like to edit?: ")
    movie_menu.edit_rating(name)

def remove_movie():
    for item in movie_menu:
        print(item.name)
        name = input("What is the name of the movie you're removing: ")
        movie_menu.delete_movie(name)

def rent_movie():
    print("Lets rent a movie for you today!: ")
    rent_movie = Rent()
    continue_order = "y"
    while continue_order == "y":
        name = input("What movie do you want?: ")
        quantity = input("How many copies?: ")
        rent_movie.add_to_cart(name, quantity)
        print(rent_movie.add_to_cart)
        print(rent_movie.total_cost())

option = ""

while option != "6":
    # system("clear")
    option = print_options()
    # system("clear")
    #print works!
    if option == "1":
        movie_menu.print_movie_menu()
    #add movie works
    elif option == "2":
        add_movie()
    elif option == "3":
        edit_rating()
    elif option == "4":
        remove_movie()
    elif option == "5":
        rent_movie()
    elif option == "6":
        continue
    else: print("Sorry, i didnt understand that input type!")

    # input("Press Enter to continue!!: ")
    # system("clear")

print("Goodbye")
