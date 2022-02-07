from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# configure window
window = Tk()
window.title("password-manager")
window.config(pady=100, padx=100)

# configure img canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# configure website UI elements
website_label = Label(text="website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# configure email/username UI elements
username_label = Label(text="email/username: ")
username_label.grid(row=2, column=0)
username_entry = Entry(width=35)
username_entry.insert(0, "test@email.com")
username_entry.grid(row=2, column=1, columnspan=2)

# configure password UI elements
password_label = Label(text="password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)
password_button = Button(text="generate password")
password_button.grid(row=3, column=2)

# configure submit button UI element
submit_button = Button(text="add", width=33)
submit_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
