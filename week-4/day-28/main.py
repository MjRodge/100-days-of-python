from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        countdown(short_break_secs)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global ticks
    count_min = math.floor(count/60)
    count_sec = count % 60
    # appends a leading zero when seconds are below 10
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # adds "00" to end of timer if clock shows whole minute
    if count_sec == 0:
        count_sec = "00"
    # prevent counter going negative
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer()
        for _ in range(math.floor(reps/2)):
            ticks += "✔"



# ---------------------------- UI SETUP ------------------------------- #
# configure window
window = Tk()
window.title("pomodoro")
window.config(pady=100, padx=100, bg=YELLOW)

# configure canvas for tomato image/counter text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 18, "bold"))
canvas.grid(row=1, column=1)

# label above tomato image
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
timer_label.grid(row=0, column=1)

# button to start timer
start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)


def clicked_reset():
    pass

# button for resetting timer
reset_button = Button(text="reset", command=clicked_reset)
reset_button.grid(row=2, column=2)

# checkmarks to show how many cycles have been completed
checkmarks = Label(text=ticks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(row=3, column=1)

# start window event listener
window.mainloop()
