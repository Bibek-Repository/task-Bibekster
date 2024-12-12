import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Use the globally defined Entry widgets to get user input
    name = entry_name.get()
    address = entry_address.get()
    phone = entry_phone.get()
    email = entry_email.get()
    password = entry_password.get()

    # Example: Show a confirmation message with the entered details
    messagebox.showinfo("Form Submitted", f"Name: {name}\nAddress: {address}\nPhone: {phone}\nPassword: {password}")

# Create the main application window
root = tk.Tk()
root.title("User Information Form")
root.geometry("300x250")

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

# Run the application
root.mainloop()
