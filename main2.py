import random

def action():
    options = ["check for a movie", "rent a movie", "randomly select a movie"]
    print("Welcome to our movie database!")
    print("\nChoose an option from the list below or q/enter to quit: ")
    for i in options:
        print(i)
    action = input("What would you like to do? ")
    return action

def get_movie_name():
    movie_name = input("What movie do you want to rent? ")
    return movie_name

#------------------------------------------------------------------------------------------#
                                #FUNCTIONAL AS OF COMMIT 4
movie_list = ['Haunted house', 'The ritual', 'Stalker', 'The Kidnapping', 'Torture']
for i in range(len(movie_list)):
    movie_list[i] = movie_list[i].lower()
    

#-------------main program func
def main():
    if action == "q":
        exit()
#---------------begin to take input. find out what user wants to do
actions= action()
#-----------------------option for random selected movie
if actions == "random":
    x = random.choice(movie_list)
    print("Watch this movie: ")
    print(x)
#-----------------------------option to check movie list
if actions == "check":
    print(movie_list)
#-------------------------------option to rent movie
if actions == "rent":
    while True:
        try:
            card_info = int(input("Please enter card information: "))
        except ValueError:
            print("Sorry, i didnt understand that. Enter numbers only")
        else:
            #input is correct, can continue
            break
    print(f"You entered: {card_info}")
    print(movie_list)
    movie_name = get_movie_name()

    if movie_name in movie_list:
        print("You got it. Enjoy and see you next time!")
#--------------call main func to begin program
    main()
#------------------------------------------------------------------------------------------#

