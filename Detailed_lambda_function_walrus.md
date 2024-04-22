The warning you're seeing in Visual Studio Code regarding "does not return a value" stems from how Python functions and methods are expected to be used in the context of a lambda expression. Essentially, the issue is about how the lambda expression is structured and used, particularly with regard to the placement and use of methods that do not return values within an expression that should evaluate to a single value.

In Python, the lambda function is expected to have a single expression which is returned. However, in your code, you're not just returning a value but also trying to perform side effects (like root.destroy(), entry_username.delete(0, tk.END), and entry_password.delete(0, tk.END)) within the lambda. Python allows you to do this using the comma to separate multiple expressions, which forms a tuple that is the actual result of the lambda. However, this is not an ideal or clear way to write code, especially since some of these functions (delete and destroy) do not return values and thus contribute None to the tuple.

To clean this up and resolve the warnings, you can refactor your code to separate side effects from the function return in the lambda. Here’s a suggested way to refactor this part:

``` py
def create_account():
    t2 = tk.Toplevel(main_frame)
    t2.geometry("200x150")  # Size the Toplevel window
    
    tk.Label(t2, text="Username").pack()
    t2_entry_username = tk.Entry(t2)
    t2_entry_username.pack()

    tk.Label(t2, text="Password").pack()
    t2_entry_password = tk.Entry(t2, show="*")
    t2_entry_password.pack(pady=(20,5))

    # Use a function directly instead of lambda
    t2_create_button = tk.Button(t2, text="Create", command=lambda: attempt_create_account(t2, t2_entry_username, t2_entry_password))
    t2_create_button.pack()

def attempt_create_account(t2, username_entry, password_entry):
    # Get user inputs
    username = username_entry.get()
    password = password_entry.get()

    # Try to sign up with the provided credentials
    result = U.sign_up(username, password)

    # Show the result in a message box
    messagebox.showinfo("Sign Up Result", result)

    # Handle the response
    if result == "Account successfully created":
        t2.destroy()
    else:
        # Clear the entries and refocus if not successful
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()

```

### Explanation:

- **Creating a New Function (attempt_create_account)**: This function accepts three arguments: the Toplevel window (t2), and the username and password entry widgets. It encapsulates the functionality that was inside the lambda function, making the code more structured and easier to follow.
- **Command Assignment**: Instead of using a lambda to handle the button press, the button's command is directly linked to attempt_create_account. A lambda is still used, but only to pass the necessary arguments to attempt_create_account. This keeps the definition of the button clean and separates the event handling logic into its own function.
- **Simplified Button Command**: The use of a named function for the command improves readability by removing the inline lambda code, which can be less clear, especially for those unfamiliar with Python's lambda syntax.

This refactoring makes the code more modular and easier to understand, maintain, and test.


Please, see below the refactoring of `login` combination of lambda function and walrus, as well:

``` py
def handle_login():
    result = U.login(entry_username.get(), entry_password.get())
    messagebox.showinfo("Login Result", result)
    if result == "Login successful":
        root.destroy()
    else:
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_username.focus()

login_button = tk.Button(login_frame, text="Login", command=handle_login)
```

### Explanation:

- **Separation of Logic**: The handle_login function handles the login attempt and subsequent UI updates. It checks the login result, shows a message box, and conditionally destroys the root window or resets the form fields.
- **Lambda Removal**: By moving the logic to a separate function, you avoid the complexities and warnings associated with using lambda for multiple statements.
