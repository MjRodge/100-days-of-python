import tkinter

window = tkinter.Tk()
window.title("this is my first gui")
window.minsize(width=800, height=500)

my_label = tkinter.Label(text="this is a label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
