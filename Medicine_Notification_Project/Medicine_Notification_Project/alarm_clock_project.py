# This is my final project file ###


# Importing all the needed packages
from tkinter.ttk import *
from tkinter import *

from time import sleep
from datetime import datetime
from pygame import mixer
from threading import Thread

# For image support
from PIL import ImageTk, Image

# Colours for Window

# light grey
bg_color = '#FAF9F6'
# dark grey
line_colour = "#5A5A5A"
# medium grey
body_colour = "#939799"
# dark teal blue
notification_bg = "#11bfb1"

# create window for Alarm Clock
window = Tk()

# notice at top of window
window.title("Alarm:")
window.geometry('550x400')
window.configure(bg=bg_color)

# lining around frame of window
frame_line = Frame(window, width=500, height=8, bg='black')
frame_line.grid(row=0, column=0)

# body of the frame within the window customizations
frame_body = Frame(window, width=550, height=400, bg=body_colour)
frame_body.grid(row=0, column=0)

# Image of Clock for window
image = Image.open('.idea/clock_image.png')
image.resize((35, 35))

image = ImageTk.PhotoImage(image)
application_Image = Label(frame_body, image=image)
application_Image.place(x=5, y=10)

# Heading on window page
name = Label(frame_body, text="Set Notification", height=2, font='Ivy 18 bold', bg=notification_bg)
name.place(x=115, y=15)

# Alarm time title text
hour = Label(frame_body, text="Alarm Time: ", height=1, font='Ivy 16 bold', bg=line_colour, fg=bg_color)
hour.place(x=125, y=85)

# label from hour
hour = Label(frame_body, text="Hour: ", height=1, font='Ivy 16 bold', bg=line_colour, fg=bg_color)
hour.place(x=125, y=145)

# hour setting:
c_hour = Combobox(frame_body, width=4, font='arial 15')
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=125, y=175)

# label for minutes
min_print = Label(frame_body, text="Min:   ", height=1, font='Ivy 16 bold', bg=line_colour, fg=bg_color)
min_print.place(x=195, y=145)

# setting minutes:
c_min = Combobox(frame_body, width=4, font='arial 15')
c_min['values'] = (
    "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
    "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38",
    "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58",
    "59")
c_min.current(0)
c_min.place(x=195, y=175)

# label for period of time
period = Label(frame_body, text="AM/PM: ", height=1, font='Ivy 16 bold', bg=line_colour, fg=bg_color)
period.place(x=265, y=145)
# setting period of time
c_period = Combobox(frame_body, width=4, font='arial 15')
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=265, y=175)


# defined function to start the alarm action
def activate_alarm():
    t = Thread(target=alarm)
    t.start()


# Function to stop alarm sound
def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()


selected = IntVar()
# radio button to activate the alarm for the time selected
button = Radiobutton(frame_body, font="ivy 12 bold", value=1, text="Set Alarm", command=activate_alarm,
                     variable=selected)
button.place(x=365, y=135)


# function to play music when the conditions are meet for the alarm time and period
def sound_alarm():
    # plays sound included in folder
    mixer.music.load('buzzer.wav')
    mixer.music.play()
    selected.set(0)

    d_button = Radiobutton(frame_body, font='ivy 16 bold', value=2, text="Turn off Alarm", bg=bg_color,
                           command=deactivate_alarm, variable=selected)
    d_button.place(x=35, y=325)


# Defined function that sets conditions for alarm
def alarm():
    while True:

        # control is determined by select status (1)
        control = selected.get()

        # prints in terminal for monitoring, shows count
        print(control)

        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()

        # variable for current time
        now = datetime.now()

        # vars for current time (H,M and period)
        now_hour = now.strftime("%I")
        print(now_hour)
        now_minutes = now.strftime("%M")
        print(now_minutes)
        now_period = now.strftime("%p")
        print(now_period)
        # if statement for conditions to be meet for alarm
        if control == 1:
            if alarm_period == now_period:
                if alarm_hour == now_hour:
                    if alarm_min == now_minutes:
                        print("Alarm!")
                        # Calls function when alarm and current times are the same
                        sound_alarm()
        sleep(1)


# for pygame, for playing sound
mixer.init()

# end of window page loop
window.mainloop()
