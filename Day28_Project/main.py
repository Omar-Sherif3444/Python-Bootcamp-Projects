import  tkinter
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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
    label2.config(text="")
    canvas.itemconfig(timer_text,text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps in (1, 3, 5, 7):
        count_down(work_sec)
        label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    elif reps == 8:
        count_down(long_break)
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
    elif reps in (2, 4, 6):
        count_down(short_break)
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif int(count_sec)<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)

    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        label2.config(text=marks)

        reps=0


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=tkinter.Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
ph=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=ph)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=("arial",25,"bold"))
canvas.grid(column=1,row=1)


label=tkinter.Label(window,text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

button1=tkinter.Button(text="Start",command=start_timer)
button1.grid(column=0,row=2)

button1=tkinter.Button(text="Reset",command=reset)
button1.grid(column=2,row=2)


label2=tkinter.Label(window,font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
label2.grid(column=1,row=3)


window.mainloop()