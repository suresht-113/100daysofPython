from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "None"
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps 
    reps= 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time():
    global reps
    reps +=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # if its the 8th
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        window.attributes('-topmost', 1)
        window.lower()

    elif reps % 2 == 0:
        # if its the 2nd/4th/6th
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        window.attributes('-topmost', 1)
        window.lower()
    else:
        # if its the 1st/3rd/5th/7th
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', 1)
        window.lower()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_time()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
            check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50,"italic"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/stejaram/Downloads/100daysofPython/day28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text =canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="Start", bg=YELLOW, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, command=timer_reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=  YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
