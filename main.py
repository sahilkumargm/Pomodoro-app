from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_checkmarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_seconds = WORK_MIN * 60  # multiplying by 60 gives the number of minutes
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown_timer(long_break_seconds)
        label_timer.config(text="Take a long break", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(short_break_seconds)
        label_timer.config(text="Take a short break", fg=PINK)
    else:
        countdown_timer(work_seconds)
        label_timer.config(text="Keep working", fg=GREEN)


# work
# s break
# work
# s break
# work
# s break
# work
# l break


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_timer(seconds):
    global reps

    count_minutes = math.floor(seconds / 60)
    count_seconds = seconds % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"  # "Creating the '00' effect in the timer"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if seconds > 0:
        # Using the .after() method to call the countdown_timer() function after every 1000 ms (1000 ms = 1 s):
        global timer
        timer = window.after(1000, countdown_timer, seconds - 1)

    else:
        start_timer()
        # Adding the checkmarks:
        if reps % 2 == 0:
            number_of_checkmarks = int(reps / 2)
            label_checkmarks.config(text=f"✓" * number_of_checkmarks)

        # # Alternate way of adding the checkmarks:
        # marks = ""
        # work_sessions = math.floor(reps/2)
        # for _ in range(work_sessions):
        #     marks += "✓"
        # label_checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)  # fg = foreground (color)
label_timer.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")  # The PhotoImage() method is the data type that
# tkinter works with when using images.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # Creating a canvas of size 200x224. A
# canvas allows you to overlay multiple
# elements
canvas.create_image(100, 112, image=tomato_img)  # The .create_image() method creates an image in the canvas. There are
# many .create_#something methods in the tkinter class that creates a new item overlay on screen. Here, 102, 112 is the
# x and y position of where the text should go. (In this case, it's the middle).
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))

canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label_checkmarks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
label_checkmarks.grid(column=1, row=3)

window.mainloop()
