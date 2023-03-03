import tkinter as tk


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

# Create the username label and entry
username_label = tk.Label(root, text="Username")
username_label.grid(row=0, column=0, sticky="W")
username = tk.Entry(root)
username.grid(row=0, column=1)

# Create the password label and entry
password_label = tk.Label(root, text="Password")
password_label.grid(row=1, column=0, sticky="W")
password = tk.Entry(root, show="*")
password.grid(row=1, column=1)

# Create the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create the result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
