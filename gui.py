import tkinter as tk
from tkinter import messagebox

def login_attempt(username, password, login_callback):
    if login_callback(username, password):
        messagebox.showinfo("Login Success", "You have successfully logged in.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def register_user(username, password, email, name, register_callback):
    if register_callback(username, password, email, name):
        messagebox.showinfo("Registration Success", "You have successfully registered.")
    else:
        messagebox.showerror("Registration Failed", "Username already taken or error in registration.")

def create_login_and_registration_form(login_callback, register_callback):
    root = tk.Tk()
    root.title("Login and Registration")

    frame_login = tk.Frame(root, bd=2)
    frame_registration = tk.Frame(root, bd=2)

    frame_login.pack(side='right', fill='both', expand=True)
    frame_registration.pack(side='left', fill='both', expand=True)

    tk.Label(frame_login, text="Login").pack()
    tk.Label(frame_login, text="Username:").pack()
    login_username_entry = tk.Entry(frame_login)
    login_username_entry.pack()

    tk.Label(frame_login, text="Password:").pack()
    login_password_entry = tk.Entry(frame_login, show="*")
    login_password_entry.pack()

    login_button = tk.Button(frame_login, text="Login", command=lambda: login_attempt(login_username_entry.get(), login_password_entry.get(), login_callback))
    login_button.pack()

    tk.Label(frame_registration, text="Register").pack()
    tk.Label(frame_registration, text="Username:").pack()
    reg_username_entry = tk.Entry(frame_registration)
    reg_username_entry.pack()

    tk.Label(frame_registration, text="Password:").pack()
    reg_password_entry = tk.Entry(frame_registration, show="*")
    reg_password_entry.pack()

    tk.Label(frame_registration, text="Email:").pack()
    email_entry = tk.Entry(frame_registration)
    email_entry.pack()

    tk.Label(frame_registration, text="Name:").pack()
    name_entry = tk.Entry(frame_registration)
    name_entry.pack()

    register_button = tk.Button(frame_registration, text="Register", command=lambda: register_user(reg_username_entry.get(), reg_password_entry.get(), email_entry.get(), name_entry.get(), register_callback))
    register_button.pack()

    root.mainloop()

