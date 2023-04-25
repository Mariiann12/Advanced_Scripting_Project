import tkinter
from tkinter.ttk import *
from tkinter import *

from IPython.terminal.pt_inputhooks import tk
from PIL import ImageTk, Image

# light grey
bg_color = '#FAF9F6'
# Dark grey
line_colour = "#5A5A5A"
# medium grey
body_colour = "#32a8a2"


def alarmextra(frame_body):
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


# create window for notification class
class alarmClock():
    window = Tk()
    window.title("Medication Notice:")

    # window.pack()
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

    selected = IntVar()

    button = tkinter.Button(frame_body, font="ivy 12 bold", text="Set Alarm", bg='#32a887')
    button.place(x=365, y=125)

    button = tkinter.Button(frame_body, font="ivy 12 bold", text="Add Alarm", bg='#32a887', command=tk.alarmextra)
    button.place(x=455, y=25)

    window.mainloop()


alarmClock();
