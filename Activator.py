from tkinter.ttk import *
from tkinter import *

from pygame import mixer


window = Tk()
window.title("")
window.geometry('350x150')


window.mainloop()


def sound_alarm():
    mixer.music.load('buzzer.wav')
    mixer.music.play()

mixer.init()
sound_alarm()


window.mainloop()