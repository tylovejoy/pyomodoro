import tkinter as tk
from tkinter import messagebox
import time

# create base window
top = tk.Tk()
top.title("Pyomodoro")
top.geometry("300x100")

# create timer visual
timer_frame = tk.Frame(top)
timer_frame.pack()
button_frame = tk.Frame(top)
button_frame.pack()

minute = tk.StringVar(top, "25")
second = tk.StringVar(top, "00")

minuteEntry = tk.Entry(timer_frame, width=2, font=("Terminal", 50, ""), textvariable=minute)
minuteEntry.pack(side=tk.LEFT)
secondEntry = tk.Entry(timer_frame, width=2, font=("Terminal", 50, ""), textvariable=second)
secondEntry.pack(side=tk.LEFT)


def countdown():
    user_answer = True
    while user_answer:

        count = 25 * 60  # 25 minutes * 60 seconds
        while count >= 0:
            mins, secs = divmod(count, 60)

            minute.set(f"{mins:02d}")
            second.set(f"{secs:02d}")

            top.update()
            time.sleep(1)

            if count == 0:
                messagebox.showinfo("Time Countdown", "Stop working! Time to take a break.")
                break

            count -= 1

        count = 5 * 60  # 5 mintes * 60 seconds
        while count >= 0:
            mins, secs = divmod(count, 60)

            minute.set(f"{mins:02d}")
            second.set(f"{secs:02d}")

            top.update()
            time.sleep(1)

            if count == 0:
                user_answer = messagebox.askyesno("Timer Countdown", "Break is over! Would you like to being working?")
                break

            count -= 1


begin_count_button = tk.Button(button_frame, text='Start', bd='5', command=countdown)
begin_count_button.pack()

top.mainloop()
