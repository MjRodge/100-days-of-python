from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # select a range of random letters, symbols, and numbers from data arrays
    selected_letters = [choice(letters) for n in range(0, randint(8, 10))]
    selected_symbols = [choice(symbols) for n in range(0, randint(2, 4))]
    selected_numbers = [choice(numbers) for n in range(0, randint(2, 4))]
    # combine generated lists into one and shuffle contents
    password_list = selected_letters + selected_symbols + selected_numbers
    shuffle(password_list)
    # join list into a string
    generated_password = "".join(password_list)
    # insert password into UI entry box
    password_entry.insert(0, generated_password)
    # copy password to clipboard
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    # validate no fields have been left empty
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="no empty fields", message="all fields must be filled")
    else:
        # write credentials to txt file
        with open("my_pass.json", "r") as json_data_file:
            # json.dump(new_data, json_data_file, indent=4)
            data = json.load(json_data_file)
            data.update(new_data)
        with open("my_pass.json", "w") as json_data_file:
            json.dump(data, json_data_file, indent=4)
            # to_txt.write(f"website: {website} | username: {username} | password: {password}\n")
        # empty the contents of website/password
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        # add focus to top entry box, website
        website_entry.focus()


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
password_button = Button(text="generate password", command=generate_password)
password_button.grid(row=3, column=2)

# configure submit button UI element
submit_button = Button(text="add", width=33, command=save)
submit_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
