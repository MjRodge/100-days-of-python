from tkinter import *

# windows
window = Tk()
window.title("this is my first gui")
window.minsize(width=800, height=500)
window.config(padx=50, pady=50)

# labels
my_label = Label(text="this is a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


# buttons
def button_click():
    my_label.config(text=my_input.get())


my_button = Button(text="click me", command=button_click)
my_button.grid(row=1, column=1)

new_button = Button(text="new button", command=button_click)
new_button.grid(row=0, column=2)
# entry
my_input = Entry()
my_input.grid(row=2, column=3)



window.mainloop()
