import tkinter as tk
from tkinter import messagebox
from sign_up_login import *

root = tk.Tk()
root.title("Sign Up and Login")
root.geometry("350x250")

# Create a main frame to center all content
main_frame = tk.Frame(root)
main_frame.pack(expand=True)


def create_account():
    t2 = tk.Toplevel(main_frame)
    t2.title("Create account")
    t2.geometry("200x150")  # Size the Toplevel window
    
    tk.Label(t2, text="Username").pack()
    t2_entry_username = tk.Entry(t2)
    t2_entry_username.pack()

    tk.Label(t2, text="Password").pack()
    t2_entry_password = tk.Entry(t2, show="*")
    t2_entry_password.pack(pady=(20,5))

    t2_create_button = tk.Button(t2, text="Create", command=lambda: (
        messagebox.showinfo("Sign Up Result", result := U.sign_up(t2_entry_username.get(), t2_entry_password.get())),
        t2.destroy() if result == "Account successfully created" else (
            t2_entry_username.delete(0, tk.END),
            t2_entry_password.delete(0, tk.END),
            t2_entry_username.focus()
        )
    ))
    t2_create_button.pack()

# Create a welcome message
welcome_label = tk.Label(main_frame, text="Welcome to our new application", font=("Helvetica", 12))
welcome_label.pack(pady=(10, 5))

# Additional instructions
instructions_label = tk.Label(main_frame, text="Please, if you have no registered account first 'Sign Up'", font=("Helvetica", 10))
instructions_label.pack(pady=(0, 10))

# Create a subframe for login controls
login_frame = tk.Frame(main_frame)
login_frame.pack(pady=20)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=10)
entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=10)
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1)

# Buttons for login and sign up
login_button = tk.Button(login_frame, text="Login", command=lambda: (
    messagebox.showinfo("Login Result", result := U.login(entry_username.get(), entry_password.get())),
    root.destroy() if result == "Login successful" else (
        entry_username.delete(0, tk.END),
        entry_password.delete(0, tk.END),
        entry_username.focus()
    )
))
login_button.grid(row=2, column=0, columnspan=2, pady=10)

sign_up_button = tk.Button(login_frame, text="Sign Up", command=lambda: create_account())
sign_up_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
