import tkinter as tk
from tkinter import font


def login():
    # Check if the entered username and password match
    if username.get() == "admin" and password.get() == "password":
        # Login successful
        result_label.config(text="Login Successful", fg="green")
    else:
        # Login failed
        result_label.config(text="Login Failed", fg="red")


# Create the main window
root = tk.Tk()
root.title("Login Form")
root.config(bg="#f0f0f0")

# Create the username label and entry
username_label = tk.Label(root, text="Username",
                          bg="#f0f0f0", font=("Segoe UI", 14))
username_label.grid(row=0, column=0, padx=20, pady=20, sticky="W")
username = tk.Entry(root, font=("Segoe UI", 14))
username.grid(row=0, column=1, padx=20)

# Create the password label and entry
password_label = tk.Label(root, text="Password",
                          bg="#f0f0f0", font=("Segoe UI", 14))
password_label.grid(row=1, column=0, padx=20, pady=20, sticky="W")
password = tk.Entry(root, show="*", font=("Segoe UI", 14))
password.grid(row=1, column=1, padx=20)

# Create the login button
login_button = tk.Button(root, text="Login", command=login, font=(
    "Segoe UI", 14), bg="#0078d7", fg="white")
login_button.grid(row=2, column=0, columnspan=2, pady=20)

# Create the result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Segoe UI", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()
