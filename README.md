# Python_OOP_GUI_Tkinter
Intro to Python OOP - Sign Up and Login form

## Intro to Python OOP (**O**bject-**O**riented **P**rogramming)

Welcome to the adventure and attempt to explain the concept of OOP in Python as clearly as possible.
The following example is simple at first glance, but it allows you to get to know other interesting terms in addition to OOP, such as:

1. list comprehension 
2. lambda function
3. walrus operator 
4. working with textual files (opening, reading, writing, appending)
5. Python's GUI (which stands for Graphical User Interface) as a Tkinter

> [!NOTE]
> walrus operator (:=) is available from Python 3.8 onwards, so you have to install Python 3.8 and newer versions


## Let's begin our adventure!

The project will be about the simplest form of sign-up and login, whereas a primitive database will be created as a textual file.

> [!CAUTION]
> Using textual files as primitive databases is just for educational purposes and can not be used in real applications and productions!
> Text files don't provide any mechanisms for ensuring data integrity or security, like transactional support or encryption!

Our project (folder "Sign_Up_and_Login_form") will have 3 files:

1. textual one "users.txt"
2. Python one "sign_up_login.py"
3. GUI Python one "GUI_sign_up_login.py"

or

<pre>/Sign_Up_and_Login_form  
 ┬  
 ├ users.txt 
 ├ sign_up_login.py 
 ├ GUI_sign_up_login.py
 </pre>


As already said:
1. the textual file `users.txt` will serve us as a primitive database in which the user's data, username, and password will be entered (of course, you can later add the user's attributes as desired, first name, last name, email, etc.)
2. the first Python code `sign_up_login.py` will include 2 classes, the first class is `User` and the second class is `Users`
3. in the second Python file `GUI_sign_up_login.py` we will connect the classes from the previous Python file to the Python GUI (Tkinter) and run our program

You can use any editor that you prefer for this project:
1. IDLE
2. VSCode (Visual Studio Code)
3. Pycharm...


### Sign Up and Login form
 

- [x] First, we will create (on "Desktop" or any disc you prefer) an empty folder and name it `Sign_Up_and_Login_form`
- [x] Then inside it, we will create a text file, `users.txt` (to open this file you can use "Notepad", as well). 
- For a detailed explanation of this file please see [Detailed textual file](About_textual_file.md)
- Original textual file `users.txt` you can find here [Original textual file](users.txt)
- [x] Now, in the same folder you should create a Python file `sign_up_login.py`. 
- For a detailed explanation of this file please see [Detalied Python file with classes](Detailed_Python_file_with_classes.md)
- Original Python file `sign_up_login.py` you can see here [Original Python file with classes](sign_up_login.py)
- [x] at the end create in the same folder the second Python file `GUI_sign_up_login.py`. 
- For a detailed explanation of this file please see [Detailed Explanation of Python GUI file](Detailed_Python_GUI_file.md)
- Original Python file `GUI_sign_up_login.py` you can see here [Original Python GUI file](GUI_sign_up_and_login.py)

> [!NOTE]
> Of course, all folder and file names are arbitrary, so you can give them other names if these are illogical to you
  
How does the program work when run?

1. if the user has no account he should first press the button "Sign Up" and a new window will be opened
2. then the user fills in "Username" and "Password" (at this level, the program has no restrictions on which and how many characters the user can use, but short names are recommended, e.g. "John123" for username and "123" for password)
3. if he did not choose an already existing username (which in this case serves as a unique identifier), after pressing the "Create account" button, he will receive a message that the account has been successfully created and will be returned to the initial window, where he will now be able to log in with the created username and password. Otherwise, if he chooses a username that already exists in our database (text file "users.txt), he will receive a message that the username is already taken and that he must enter another one.
4. After creating an account or if the user has already created an account when he tries to log in in case he has forgotten his username or password, he will receive appropriate messages.

Of course, as we said at the beginning, this is one of the simplest examples of the "Sign Up and Login" form, so the program can be further upgraded as follows:
1. that the user, if he does not fill in one of the fields offered, receives a message that he must do so
2. to create a "Forgotten password" button, where the user will be allowed to create a new password
3. to set conditions regarding the type of characters that can be used to create passwords and usernames, as well as the length of passwords and usernames, minimum and/or maximum characters
4. that the program itself offers the user the appropriate password,
5. as well as that the program evaluates the strength of the password created by the user himself
6. limit login attempts to a maximum of 3 due to a forgotten password or incorrectly entered username etc.
