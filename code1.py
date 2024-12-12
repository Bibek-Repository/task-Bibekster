import tkinter as tk
from tkinter import messagebox
import database
from tkinter import ttk
from tkinter import Tk
from database import initialize_database, insert_data, fetch_all_data
from tkinter.ttk import Treeview

# Create the main application window
root = Tk()
root.title("Data Entry Form")
root.geometry("500x500")

# Treeview widget to display data
tree = Treeview(root, columns=("ID", "Name", "Address", "Phone", "Email", "Password"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Address", text="Address")
tree.heading("Phone", text="Phone")
tree.heading("Email", text="Email")
tree.heading("Password", text="Password")
tree.pack()

def submit_form():
    # Use the globally defined Entry widgets to get user input
    name = entry_name.get()
    address = entry_address.get()
    phone = entry_phone.get()
    email = entry_email.get()
    password = entry_password.get()

    if not all([name, address, phone, email, password]):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    # Insert the data into the database
    insert_data(name, address, phone, email, password)

    # Show a confirmation message with the entered details
    messagebox.showinfo("Form Submitted", f"Name: {name}\nAddress: {address}\nPhone: {phone}\nPassword: {password}")

    # Clear the input fields
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    # Initialize the database (only needed once at the start)
    database.initialize_database()

def display_data():
    # Fetch data from the database
    data = fetch_all_data()

    # Clear existing data in the treeview
    for row in tree.get_children():
        tree.delete(row)

    # Insert data into the treeview
    for row in data:
        tree.insert("", tk.END, values=row)

# Create labels and entry fields for the form
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=(10, 0))
entry_name = tk.Entry(root, width=30)
entry_name.pack()

label_address = tk.Label(root, text="Address:")
label_address.pack(pady=(10, 0))
entry_address = tk.Entry(root, width=30)
entry_address.pack()

label_phone = tk.Label(root, text="Phone Number:")
label_phone.pack(pady=(10, 0))
entry_phone = tk.Entry(root, width=30)
entry_phone.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=(10, 0))
entry_email = tk.Entry(root, width=30)
entry_email.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(10, 0))
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=(20, 0))

# Create a button to display data
display_button = tk.Button(root, text="Display Data", command=display_data)
display_button.pack(pady=(10, 0))

# Initialize the database (called once)
initialize_database()

# Run the application
root.mainloop()
