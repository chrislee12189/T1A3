from Movie_Menu import Movie_Menu
from Movie_menu_items import Movie_Menu_Items


#------------------------------------MOVIE NAMES AND RATINGS-------------------------------------------------------#
def movie_seed():
    movie1 = Movie_Menu_Items("The Haunting", 5)
    movie2 = Movie_Menu_Items("The Ritual", 4)
    movie3 = Movie_Menu_Items("Necromancers", 5)
    movie4 = Movie_Menu_Items("Kidnapping", 3)
    movie5 = Movie_Menu_Items("Slaughterhouse", 2)
    movie6 = Movie_Menu_Items("Stalker", 1)
    movie_menu = Movie_Menu([movie1, movie2, movie3, movie4, movie5, movie6])
    return movie_menu
