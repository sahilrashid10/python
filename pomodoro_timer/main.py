from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    if timer is not None:  # Check if a timer exists
        window.after_cancel(timer)
    # don't use straight config here too (doesn't work)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="TIMER")
    check_mark.config(text="")
    global reps
    global tick
    reps = 0
    tick = 1
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if timer is None:
        global reps
        reps += 1
        global tick
        if reps % 8 == 0:
            tick = 1
            check_mark.config(text="")
            count_down(LONG_BREAK_MIN * 60)
            top_label.config(text="Long Break")
        elif reps % 2 == 0:
            check_mark.config(text="✅" * tick)
            count_down(SHORT_BREAK_MIN * 60)
            top_label.config(text="Short Break")
            tick += 1
        else:
            count_down(WORK_MIN * 60)
            top_label.config(text="Time to Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    rem_min = math.floor(count / 60)
    rem_sec = count % 60
    if rem_sec < 10:
        rem_sec = f"0{rem_sec}"
    # TODO: using the below line to config canvas, we couldn't directly do it
    canvas.itemconfig(timer_text, text=f"{rem_min}:{rem_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("sr7_POMODORO")
window.config(padx=100, pady=50, bg=RED)

# adding an image
canvas = Canvas(width=200, height=200, bg=PINK)
# TODO: can't directly put image location inside create_image
cat_img = PhotoImage(file="cat.png")
canvas.create_image(100, 65, image=cat_img)

timer_text = canvas.create_text(103, 147, text="00:00", font=(FONT_NAME, 25))
canvas.grid(row=2, column=2)

top_label = Label(text="TIMER", fg="white", bg=RED, font=(FONT_NAME, 20, "bold"))
top_label.grid(row=1, column=2)

button1 = Button(text="START", command=start_timer)
button1.grid(row=3, column=1)

check_mark = Label(bg=RED, fg="black", font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=2)

reset_button = Button(text="RESET", command=reset)
reset_button.grid(row=3, column=3)

window.mainloop()
