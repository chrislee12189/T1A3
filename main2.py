from Movie_menu_items import Movie_Menu_Items
from Movie_Menu import Movie_Menu
from seed import movie_seed


movie_menu = movie_seed
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
    price = float(input(f"Whats the price of {name}?: "))
    Movie_Menu.add_item(name, price)

def remove_movie():
    for item in movie_seed:
        print(item.name)
        name = input("What is the name of the movie you're removing: ")
        movie_seed.delete_movie(name)





































































# import random
# from os import system

# def action():
#     options = ["check for a movie", "rent a movie", "randomly select a movie"]
#     print("Welcome to our movie database!")
#     print("\nChoose an option from the list below or q/enter to quit: ")
#     for i in options:
#         print(i)
#     action = input("What would you like to do? ")
#     return action

# def get_movie_name():
#     movie_name = input("What movie do you want to rent? ")
#     return movie_name

# #------------------------------------------------------------------------------------------#
#                                 #FUNCTIONAL AS OF COMMIT 4
# movie_list = ['Haunted house', 'The ritual', 'Stalker', 'The Kidnapping', 'Torture']
# for i in range(len(movie_list)):
#     movie_list[i] = movie_list[i].lower()
    

# #-------------main program func
# def main():
#     if action == "q":
#         exit()
# #---------------begin to take input. find out what user wants to do
# actions= action()
# #-----------------------option for random selected movie
# if actions == "random":
#     x = random.choice(movie_list)
#     print("Watch this movie: ")
#     print(x)
# #-----------------------------option to check movie list
# if actions == "check":
#     print(movie_list)
# #-------------------------------option to rent movie
# if actions == "rent":
#     while True:
#         try:
#             card_info = int(input("Please enter card information: "))
#         except ValueError:
#             print("Sorry, i didnt understand that. Enter numbers only")
#         else:
#             #input is correct, can continue
#             break
#     print(f"You entered: {card_info}")
#     print(movie_list)
#     movie_name = get_movie_name()

#     if movie_name in movie_list:
#         print("You got it. Enjoy and see you next time!")
# #--------------call main func to begin program
#     main()
# #------------------------------------------------------------------------------------------#

