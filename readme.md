# **READ ME DOCUMENTATION FOR TERMINAL APP (T1A3)**  
**DOCUMENTATION WILL INCLUDE:**  
- **DESIGN/IMPLEMENTATION**  
- **FEATURES**   
- **TESTING**  
- **TESTING RESULTS**  

# DESIGN PROCESS AND IDEAS/IMPLEMENTATION  
This terminal app is supposed to mimmic a virtual/online movie database/rental buisness.  The app currently has features in it that allow the user to navigate from a home/main menu through the program depending on what they want to do. Currently, they can check our database and find out what films we have/what films are available to rent. Users can also add a movie to the database alongside a corresponding rating.Once successfully added, users are able to see the movie they added by reprinting the movie list!  

I went through a few different ideas and functionality levels of different terminal apps before arriving at the current one thanks to a suggestion from an educator.  As a means of working as efficiently as possible, i was able to take code-along class work, rebuild it from the ground up and redesign it and further turn it into a new app.Using material i was familiar with really made me feel a lot more comfortable about this project because i was able to take what we'd learnt and play with it in a familiar environment.

The design process was made easier by collaborating with Trello; any design ideas i had were made into a card, the idea then went into production for a while until i could decide if it would make the cut or not. If the idea did not make the cut, it was moved to a tree called "scrapped functionality planning".  

Overall, a few things were used for the design process, in an effort to keep this documentation as brief as possible, the design processes used were as follows:  
- **Trello**  - (used to spitball ideas and keep track of what was implemented/what worked/didnt work)
- **Diagram/Flowcharting** - (used to visual how the app would function and communicate with itself)  
- **Slide Decks** - (used to present functionality,planning, design processes)
- **Hand written journal/drawings** - (used to quickly scribble ideas out and solve functionality issues)  

#  FEATURES  
## THE THREE FEATURES OF MY TERMINAL APP ARE:
- EDIT RATING OF MOVIE IN/ADDED TO DATABASE
- ADD MOVIE TO DATABASE
- RENT MOVIE


### **FEATURE 1:**  
My first feature is the "Edit Rating" feature. In my program, there is a predefined list with 6 or so movies. All of these movies come with a preassigned rating. Users are able to edit the rating of this movie by selecting the "edit rating" option from the main menu. They will then be prompted to provide the name of the movie they are editing as well as the new rating they are assigning to it.   
Users are also able to edit the rating of a movie they have added via the same methodology.  

### **FEATURE 2:**  
My second feature is the "Add a movie" feature. Users are able to select this option from the main menu. The program will prompt them to provide a name and a rating for the movie they're adding.  

### **FEATURE 3:**  
My third feature is the "Rent a movie". Users are able to choose a movie from the list and choose how long they wish to rent the movie for. There is a maximum rental allowance length of 19 days. Should users exceed that length when they are prompted, they will be denied rental.  

### **HONOURABLE MENTIONS:**  
Users also have the ability to delete movies from the list. They are able to delete movies that were already present when the program began and/or movies that they've added themselves.  
Users can also see the menu at any time by following the prompt to display the menu.  

## HOW MY FEATURES WORK:  
### FEATURE 1:  
``` 
    def edit_movie_rating(self, name):
        for item in self.movie_menu_items:
            if item.name == name:
                rating = float(input(f"What is the updated rating of {name}?: "))
                item.rating = rating
                return print(f"{name}'s rating was updated!")
        return print(f"{name} is not in our database!")
```  

```
def edit_rating():
    movie_menu.print_movie_menu()
    name = input("Whats the name of the movie who's rating youd like to edit?: ")
    movie_menu.edit_movie_rating(name)
```

### edit_movie_rating:
- The edit_movie_rating feature utilises a "for" loop to iterate over the list of movies that is has. (Includes movies added by the user)  
- The "for" loop then has a conditional "if" statement that checks user input against the list of movies.  
- *If* the name the user provided matches a known movie name, the program proceeds to prompt them to provide the new rating.  
- Type conversion converts user input into a float in case they decide to use a decimal number for the rating.  
- Item_rating = rating assigns the new rating to a variable  
- 2 return statements are present in this code block, the first, is nested and prompts the user of a successful rating update. The second is outside the loop and returns a failed search for the movie they were looking to edit.  

### edit_rating:  
- This function is much simpler. First it prints the movie list  
- Then it prompts the user and asks for the movie they wish to edit.  
- Using the dot notation, the program can access the attributes/methods of the Movie_menu class. This class and its functions were imported to main so that i could envoke them/or access each method of instances of different object classes.  


### FEATURE 2: 
```
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
```
```
    def add_movie(self, name, rating):
        new_item = Movie_Menu_Items(name, rating)
        self.movie_menu_items.append(new_item)
```
### add_movie:  
- This function takes user input and converts it into a string. The reason for this type conversion is because movie names can include numbers.  
- In the first *try* test block, the program checks to see if the user entered something when prompted for an input.  
- If the input is empty/they didnt enter anything, the program prompts the user by telling them it is an invalid entry. Catching an empty string works efficiently and so the valueerror is never raised.  
- The program then asks the user for the rating of the movie they're adding. This number is converted to a float in case they enter a decimal number.  
- If they enter anything but an integer for the rating, the program alerts them that this is an invalid entry and they will be required to resubmit.

### add_movie(self,name,rating):
- This function takes the input from the user and stores it in a variable called new_item.
- The program then appends this variable to the movie menu list and so if the user prints the movie menu list after that, the new movie will be seen on the database.  

### FEATURE 3:  
```

```
```

```



EXPLAIN WHY I CHOSE THEM  
EXPLAIN HOW THEY WORK 
EXPLAIN DRAFT FEATURES/WHY THEY WERE CUT
EXPLAIN FEATURES THAT DIDNT MAKE THE CUT/SUB FEATURES

# TESTING AND TEST RESULTS  
EXPLAIN TESTS  
REFERENCE GOOGLE SHEETS TEST DOCUMENTATION  
TEST RESULTS   
RETESTS/TEST SCOPE ADJUSTING DUE TO RESULTS  

# LINKS TO GITHUB, EXTERNAL DOCUMENTATIONS SUCH AS TRELLO AND GOOGLE SHEETS