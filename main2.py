from multiprocessing.sharedctypes import Value
from os import system

# from pkg_resources import working_set
from Movie_menu_items import Movie_Menu_Items
from Movie_Menu import Movie_Menu
from seed import movie_seed
from rent import Rent

#---------------------------------------TODO:-----------------------------------------#
#edit test for menu
#-------------------------------------------------------------------------------------#

# def check_is_digit(input_str):
#     if input_str.strip().isdigit():
#         print("User input is Number")
#     else:
#         print("User input is string")


# num1 = input("Enter number and hit enter")
# check_is_digit(num1)

# num2 = input("Enter number and hit enter")
# check_is_digit(num2)

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
    try:
        name=str(input("Whats the name of the movie youre adding?: "))
        if name == "":
            print("Empty name entries are invalid. You will be required to rebsumit your entry.")
    except ValueError:
        print("ValueError detected.")
    try:
        rating = float(input(f"Whats the rating of {name}?: "))
        movie_menu.add_movie(name,rating)
    except ValueError: 
        return print("Invalid input type. Rating can only be a number. You will be required to resubmit your entry.")



def edit_rating():
    movie_menu.print_movie_menu()
    name = input("Whats the name of the movie who's rating youd like to edit?: ")
    movie_menu.edit_movie_rating(name)


def remove_movie():
        name = input("What is the name of the movie you're removing: ")
        movie_menu.delete_movie(name)


def rent_movie():
    max_length = 20
    movie_menu.print_movie_menu()
    name=input("Whats the name of the movie youre borrowing?: ")
    if name == "":
        print("Invalid option, empty entries are not allowed.")
    try:
        length = float(input(f"How long (# in days) are you borrowing {name} for?: "))
        if length >= max_length:
            print("Maximum rental period is 19 days.")
        if length == "":
            print("Invalid option, empty entries are not allowed.")
        else:
            if length <= 19:
                print(f"{name}: is loaned to you for: {length} days! Enjoy")
    except ValueError:
        print("Value Error. Rental period input must be integer.")
    

option = ""
while option != "6":
    option = print_options()
    if option == "1":
        movie_menu.print_movie_menu()
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
    else : print("Sorry, i didnt understand that input type!")
print("Goodbye")

