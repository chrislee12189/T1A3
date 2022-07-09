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

if action == "q":
    exit()
movie_list = ['Haunted house', 'The ritual', 'Stalker', 'The kidnapping', 'Torture']


actions= action()
if actions == "random":
    # movie_list = ['Haunted house', 'The ritual', 'Stalker', 'The kidnapping', 'Torture']
    x = random.choice(movie_list)
    print("Watch this movie: ")
    print(x)

if actions == "check":
    print(movie_list)

if actions == "rent":
    print("Enter your card information")
    while True:
        try:
            card_info = int(input("Please enter card information: "))
        except ValueError:
            print("Sorry, i didnt understand that. Enter numbers only")
        # continue 
        else:
            #input is correct, can continue
            break
    print(f"You entered: {card_info}")
    print(movie_list)
    movie_name= get_movie_name()
if movie_name in movie_list:
    print("You got it")
#------------------------------------------------------------------------------------------#

