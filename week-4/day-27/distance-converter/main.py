from tkinter import *

window = Tk()
window.title("miles to kilometres")
window.config(padx=50, pady=50)

mile_input = Entry(width=9)
mile_input.insert(0, 0)
mile_input.grid(row=0, column=1)

mile_label = Label(text="miles")
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

calc_label = Label(text="0")
calc_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)


def calculate_km():
    miles = float(mile_input.get())
    km = miles * 1.609344
    calc_label.config(text=str(km))


calc_button = Button(text="calculate", command=calculate_km)
calc_button.grid(row=2, column=1)

window.mainloop()
