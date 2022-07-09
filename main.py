import random

_movie_database = [
        "scary ghosts",
        "murder mystery",
        "haunted house",
        "stalker",
        "torture",
        "necromancers",
        "the conjuring"]


def _action():
    options = ["check for a movie", "rent a movie", "randomly select a movie"]
    print("Welcome to our movie database!")
    print("\nChoose an option from the list below: ")
    for i in options:
        print(i)
    action = input("What would you like to do?: ")
    return action


def _random_movie():
    random_movie = input("\nMovie name?: ")
    return random_movie


def _rent_movie():
    rent_movie = input("\nBook title?: ")
    return rent_movie


def _findmovie(catalogue, moviename):
    if moviename in catalogue[moviename]:
        return True
    else:
        return False


def _rent_movie(movie_database, author, book_title):

    if author in movie_database:

        movie_database[author].remove(book_title)
        return movie_database

    else:
        return "Item not available"


def _randomly_select():
    print(random.choice(_movie_database))
#----------------------------------------------------#


def main():

    movie_database = [
        "scary ghosts",
        "murder mystery",
        "haunted house",
        "stalker",
        "torture",
        "necromancers",
        "the conjuring"]

    action = _action()
    random_selector = _randomly_select()
    movie_finder = _findmovie()
    borrow_movie = _rent_movie()

    if action == "check":

        movie_available = _findmovie(movie_database)

        return f"Available: {_findmovie}"

    elif action == "rent":
        rent = _rent_movie(movie_database, _findmovie)

        return rent

    else:
        return random.choice[_movie_database]

main()
# result = main()

# print(result)