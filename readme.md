# **READ ME DOCUMENTATION FOR TERMINAL APP (T1A3)**  
**DOCUMENTATION WILL INCLUDE:**
- **INSTALLATION STEPS**
- **DEPENDENCIES/MINIMUM SYSTEM REQUIREMENTS**  
- **DESIGN/IMPLEMENTATION**  
- **FEATURES**   
- **TESTING**  
- **TESTING RESULTS**  
# LINK TO MY GITHUB REPOSITORY:
https://github.com/chrislee12189/T1A3  
# LINK TO CLONE MY GITHUB REPOSITORY:
git@github.com:chrislee12189/T1A3.git 
# LINK TO GOOGLE SHEETS DOC CONTAINING TESTS
https://docs.google.com/spreadsheets/d/1efrQbJEYdCSuF6wbV7F3Qs6WEMpdF6MXvO5bObPIXcw/edit#gid=1342169021  
# LINK TO TRELLO BOARD  
https://trello.com/b/ikXsEPIs/terminal-app-t1a3
# INSTALLATION STEPS:
To install and run this program:  
- Create a new directory on your terminal  ("mkdir" followed by the name you want to call the directory)
- Once this new directory is created, copy the link above (my github repository clone link)
- Paste git@github.com:chrislee12189/T1A3.git into your terminal and hit enter
- Wait for the repository to clone
- The command python3 main2.py will execute the program. (**NOTE:** command may also "python main2.py)  
- The program will begin from the main menu. You can navigate through menu options using the numeric number associated with the menu option. ie 1.Print options = press "1" and click enter 

# DEPENDENCIES/REQUIREMENTS/SYSTEM HARDWARE
- There is no minimum hardware requirements needed to run this app
- Link to colorama module: https://www.youtube.com/watch?v=u51Zjlnui4Y&ab_channel=TechWithTim
- In order for the colored text effects to work in terminal you will need install them. Installation is as easy as entering this command into your terminal: 
```
pip install colorama
```
### OR
```
pip3 install colorama
```
- access to terminal or bash shell required
# DESIGN PROCESS AND IDEAS/IMPLEMENTATION  
This terminal app is supposed to mimmic a virtual/online movie database/rental buisness.  The app currently has features in it that allow the user to navigate from a home/main menu through the program depending on what they want to do. Currently, they can check our database and find out what films we have/what films are available to rent. Users can also add a movie to the database alongside a corresponding rating.Once successfully added, users are able to see the movie they added by reprinting the movie list!  

I went through a few different ideas and functionality levels of different terminal apps before arriving at the current one thanks to a suggestion from an educator.  As a means of working as efficiently as possible, i was able to take code-along class work, rebuild it from the ground up and redesign it and further turn it into a new app.Using material i was familiar with really made me feel a lot more comfortable about this project because i was able to take what we'd learnt and play with it in a familiar environment.

The design process was made easier by collaborating with Trello; any design ideas i had were made into a card, the idea then went into production for a while until i could decide if it would make the cut or not. If the idea did not make the cut, it was moved to a tree called "scrapped functionality planning".  

Overall, a few things were used for the design process, in an effort to keep this documentation as brief as possible, the design processes used were as follows:  
- **Trello**  - (used to spitball ideas and keep track of what was implemented/what worked/didnt work)
- **Diagram/Flowcharting** - (used to visual how the app would function and communicate with itself)  
- **Slide Decks** - (used to present functionality,planning, design processes)
- **Hand written journal/drawings** - (used to quickly scribble ideas out and solve functionality issues)  
### ACCESS TO TRELLO AND DIAGRAMS WILL BE PROVIDED VIA PRESENTATION, GITHUB AND SUBMITTED WITH ASSIGNMENT  

## CODE STYLE CONVENTIONS:
This terminal applicationw was written in accorance to standard python conventions.

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
```
```
class Rent:
    def __init__(self):
        self.rent_movie = {}
        
    def add_to_cart(self,name,length):
        self.name = name
        self.length = length 
        print(f"{self.name}: is loaned to you for: {self.length}")
```
### rent_movie:
- This function is responsible for accepting input from the user. If the input is empty, they get an invalid entry prompt.
- Once theyve let the program know what movie they want, they enter how long they want to borrow it for. 
- If they request to rent it for longer than 19 days, they will be denied. 
- They will also recieve a value error if they do not enter an integer for the rental length.

### class Rent:
- This class is actually on the cutting board now, im 99% i dont and will not need this class.
- It was used in earlier versions of the program but no longer seems to be used. 
- Subject to the result of functionality test, if it can be removed, it will be.
- It is included in this documentation to show the reader the thought processes i had when creating this section of the program.


## WHY WERE THESE FEATURES CHOSEN?: 
I chose these 3 features to put forward for assessment because i feel they show some fun code that features relative complexity. These features were also great canditates for testing and allowed for a broad scope of tests/outcomes.  
These features allowed for try/except testing, ValueError testing and if/else testing.  
All of these tests handle/catch errors in a different way and i feel like i learnt a lot by doing it this way.

### SUB FEATURES:
The delete_movie was a strong candidate for a feature that would be presented for assessment. Ultimately i didnt include it, but i would like to give it an honourable mention. That function has some cool features, such as the ability to iterate over the movie menu list -including movies added by the user- and remove them if selected. It features 2 conditional return statements and was a great learning curve regarding indentation conventions/functionality.  

The movie menu itself was brielfy considered for a feature due to its interaction with nearly every function in the program. It is a staple to the program but it did not allow for impressive/good testing methodology and so it was axed as a contended for a feature.

# TESTING AND TEST RESULTS  
- Each feature had 2 primary tests applied to it to test functionality and error handling.
- If the tests failed, a retest was conducted. 
- 2 features passed tests easily. 
- The 3rd feature (renting a movie) passed its first test but made me aware that the test scope should be broadened. 
- The 3rd feature passed its second test but **failed** its third test.
- The 3rd feature passed its retest.

## TESTING METHODOLOGY AND DOCUMENTATION:
- Testing was conducted via google spreadsheet and smartsheet
- Tests were documented, dated, described and graded (pass/fail)
- If a test failed, it remained on the documentation and a new row was used to demonstrate re-testing efforts.
