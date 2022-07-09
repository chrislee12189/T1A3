# import random
# _movie_database = [
#         "scary ghosts",
#         "murder mystery",
#         "haunted house",
#         "stalker",
#         "torture",
#         "necromancers",
#         "the conjuring"]


# def action():
#     options = ["check for a movie", "rent a movie", "randomly select a movie"]
#     print("Welcome to our movie database!")
#     print("\nChoose an option from the list below: ")
#     for i in options:
#         print(i)
#     action = input("What would you like to do?: ")
#     return action


# def random_movie():
#     random_movie = input("\nMovie name?: ")
#     return random_movie


# def rent_movie():
#     rent_movie = input("\nBook title?: ")
#     return rent_movie


# def findmovie(catalogue, moviename):
#     if moviename in catalogue[moviename]:
#         return True
#     else:
#         return False


# def rent_movie(movie_database, x, book_title):

#     if x in movie_database:

#         movie_database[x].remove(book_title)
#         return movie_database

#     else:
#         return "Item not available"


# def randomly_select():
#     print(random.choice(_movie_database))
# #----------------------------------------------------#


# def main():
#     action = input()

#     movie_database = [
#         "scary ghosts",
#         "murder mystery",
#         "haunted house",
#         "stalker",
#         "torture",
#         "necromancers",
#         "the conjuring"]
#     if action == "check":
#         movie_available = findmovie(_movie_database)
#         return f"Available: {findmovie}"

#     elif action == "rent":
#         rent = rent_movie(_movie_database, findmovie)

#         return rent

#     elif action == "random":
#         x = random.choice(movie_database)
#         print(x)

# main()
# # result = main()

# # print(result)action = _action()
# # random_selector = _randomly_select()
# # borrow_movie = _rent_movie()