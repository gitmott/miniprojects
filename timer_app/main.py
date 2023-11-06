from tkinter import *
import math


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05 ##usually 25
SHORT_BREAK_MIN = 0.05 ##usually 5
LONG_BREAK_MIN = 0.05 ##usually 20
reps = 0
timer = None


def countdown(count):
        
        count_min = math.floor(count/60)
        count_sec = count % 60
   
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global timer
            timer = window.after(1000, countdown, count - 1)
        else:
            check_marks = ""
            work_sessions = range(math.floor(reps/2))
            for _ in work_sessions:
                check_marks += "X"
            check_mark_label.config(text=check_marks)
            start_timer()


def short_break_timer():
    countdown(SHORT_BREAK_MIN * 60)


def long_break_timer():
    countdown(LONG_BREAK_MIN * 60)


def rest_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title_label.config(text="Timer")
    check_mark_label.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_title_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_title_label.config(text="Short break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_title_label.config(text="Work", fg=GREEN)


# UI SETUP
window = Tk()
window.title("Timer")
window.config(padx=10, pady=10, bg=YELLOW)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(103, 112, text=WORK_MIN, fill="red", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
timer_title_label.grid(row=0, column=1)

check_mark_label = Label(fg=RED, bg=YELLOW, font="bold")
check_mark_label.grid(row=3, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=rest_timer)
reset_button.grid(row=2, column=2)

window.mainloop()