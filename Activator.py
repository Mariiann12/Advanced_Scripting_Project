from tkinter.ttk import *
from tkinter import *

from pygame import mixer


window = Tk()
window.title("")
window.geometry('350x150')


window.mainloop()


def sound_alarm():
    mixer.music.load('alarm_Medication.mp3')
    mixer.music.play()

mixer.init()

window.mainloop()
