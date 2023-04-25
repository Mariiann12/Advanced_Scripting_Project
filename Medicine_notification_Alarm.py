import tkinter
from threading import Thread
from tkinter import Radiobutton
from tkinter.ttk import *
from tkinter import *

from pygame import mixer
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep

# light grey
bg_color = '#FAF9F6'
# Dark grey
line_colour = "#5A5A5A"
# medium grey
body_colour = "#32a8a2"

# create window for notification class
window = Tk()
window.title("Medication Notice:")

window.geometry('600x350')

window.configure(bg=bg_color)

frame_line = Frame(window, width=600, height=8, bg=line_colour)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=600, height=450, bg=body_colour)
frame_body.grid(row=0, column=0)

image = Image.open("Images\medicine.png")
image.resize((75, 75))
image = ImageTk.PhotoImage(image)

application_Image = Label(frame_body, height=100, image=image)
application_Image.place(x=5, y=10)

name = Label(frame_body, text="Take medication", height=2, font='Helvetica 16 bold', bg=body_colour)
name.place(x=125, y=5)

hour = Label(frame_body, text="Alarm Time: ", height=1, font='Helvetica 16 bold', bg=line_colour, fg=bg_color)
hour.place(x=145, y=75)

hour = Label(frame_body, text="Hour: ", height=1, font='Helvetica 16 bold', bg=line_colour, fg=bg_color)
hour.place(x=140, y=115)

# hour setting:
c_hour = Combobox(frame_body, width=4, font='Helvetica 16')
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=140, y=145)

# setting minutes:
mins = Label(frame_body, text="Min: ", height=1, font='Helvetica 16 bold', bg=line_colour, fg=bg_color)
mins.place(x=210, y=115)

c_min = Combobox(frame_body, width=4, font='Helvetica 16')
c_min['values'] = (
    "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
    "18",
    "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
    "38",
    "39",
    "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57",
    "58",
    "59")
c_min.current(0)
c_min.place(x=205, y=145)

period = Label(frame_body, text="AM/PM: ", height=1, font='Ivy 16 bold', bg=line_colour, fg=bg_color)
period.place(x=265, y=115)
c_period = Combobox(frame_body, width=4, font='arial 16')
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=275, y=145)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()


def deactivate_alarm():
    print('Deactivated Alarm: '(), selected.get())
    mixer.music.stop()
    selected = IntVar()

    set_alarm_button = Radiobutton(frame_body, font="ivy 12 bold", value=1, text="Set Alarm", bg='#32a887',
                                   command=activate_alarm, variable=selected)
    set_alarm_button.place(x=365, y=125)
    deactivate_alarm_button = Radiobutton(frame_body, font="ivy 12 bold", value=2, text="Turn Off Alarm", bg='#32a887',
                                          command=deactivate_alarm, variable=selected)
    deactivate_alarm_button.place(x=365, y=175)

    add_alarm_button = Radiobutton(frame_body, font="ivy 12 bold", value=0, text="Add Alarm", bg='#32a887')
    add_alarm_button.place(x=455, y=25)


def sound_alarm():
    mixer.music.load('buzzer.wav')
    mixer.music.play()
    selected.set(0)

def stop_alarm():
    print('Deactivate alarm: ', selected.get())
    mixer.music.stop()

def alarm():
    while True:
        control = selected.get()
        print(control)
        alarm_hour = c_hour.get()
        alarm_mins = c_min.get()
        alarm_pm_am = c_period.get()
        alarm_pm_am = str(alarm_pm_am).upper()

        now = datetime.now()

        hour = now.strftime("%I")
        mins = now.strftime("%M")
        pm_am = now.strftime("%p")

        if control == 1:
            if alarm_pm_am == pm_am:
                if alarm_hour == hour:
                    if alarm_mins == mins:
                        print("Take medicine")
                        sound_alarm()

        sleep(1)

    window.mainloop()
