from tkinter.ttk import *
from tkinter import *

from pygame import mixer

from datetime import datetime
from time import sleep

window = Tk()
window.title("")
window.geometry('350x150')

window.mainloop()


def sound_alarm():
    mixer.music.load('buzzer.wav')
    mixer.music.play()


def alarm():
    while True:
        control = 1
        print(control)
        alarm_hour = '01'
        alarm_mins = '25'
        alarm_pm_am = 'AM'.upper()

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

    mixer.init()
    alarm()


window.mainloop()
