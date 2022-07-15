# **HELP FILE** 
This terminal app was created for an assignment and features simple navigation capabilites, simple add/remove functionality and also a rental feature that allows the user to rent a movie.  
Navigating the program is simple:  
## MAIN MENU: 
The app begins at the main menu. Users will be greeted with an options list. To select an option, users must enter a numerical number. i.e. "1" or "2" and not "one" or "two".  
The options are:
- 1. Show movie list
- 2. Add a movie to the list
- 3. Edit the rating of a movie 
- 4. Delete a movie from the database
- 5. Rent a movie from the list

# INSTALLATION STEPS:
To install and run this program:  
- Create a new directory on your terminal  ("mkdir" followed by the name you want to call the directory)
- Once this new directory is created, copy the link above (my github repository clone link)
- Paste git@github.com:chrislee12189/T1A3.git into your terminal and hit enter
- Wait for the repository to clone
- The command python3 main2.py will execute the program. (**NOTE:** command may also "python main2.py)  
- The program will begin from the main menu. You can navigate through menu options using the numeric number associated with the menu option. ie 1.Print options = press "1" and click enter

## THE MENU IS PRINTED INCREDIBLY OFTEN AND USERS ARE ABLE TO INTERACT WITH IT AFTER ANY TASK COMPLETION, WHETHER THEY INPUT A VALID RESPONSE TO THEIR CURRENT ACTIVITY OR NOT.
### Option 1:  
Option one prints the list of movies i pre defined for the program. If a user selects "2" from the main menu and correctly adds a movie, reprinting the list will show the original list and any movie they added. These entries are only valid for the current session, ending the program and restarting it will erase any additions/deletions the user makes.

### Option 2: 
Option two allows the user to add a movie. They will be prompted for the name and the rating of the movie they want to add. In order to successfully add a movie, they need to provide a name (any str/integer is fine) and a rating (integer only). Failure to do so, the program will alert the user to this and the entry will **not** be added to the database.

### Option 3:
Option three allows the user to edit the rating of a movie. This can be either a movie theyve added (after successful addition of the movie) or a movie that is in the predefined list. Users will provide an integer to edit the rating.

### Option 4: 
Option four allows the user to delete a movie from the database, like option 3, they can delete predefined movies or movies theyve added (after theyre added of course). To remove a movie, they must provide the name. This **is** case sensitive, ignoring case sensitivity will result in a failed attempt. 

### Option 5:  
Option five allows the user to rent a movie, the criteria to rent is: movie must be in the database, rental length must be less than or equal to 19 days. To rent a movie, the user is prompted for 2 inputs, movie name and length of rental. If the movie name entry is empty, the program alerts the user and the attempt is invalid. If the rental length exceeds 19 days, it is also disallowed. A successful rental entry would be: correct in terms of case sensitivity and under the maximum number of days allowed for rent.  

### Option 6:
Option six exits the program.



## IMPORTED LIBRARIES/MODULES 
Documentation produced in the readme.md alerts users to the criteria needed for this program to function. I will place the same message here for ease of access: 
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