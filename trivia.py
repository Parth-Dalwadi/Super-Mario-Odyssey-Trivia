import json
from tkinter import *
from tkinter import ttk
import winsound


winsound.PlaySound('Music/steamGardens.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Super Mario Odyssey Trivia")
root.configure(background="black")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!", background="red").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


class Trivia:
    def __init__(self):
        self


root.mainloop()
winsound.PlaySound(None, winsound.SND_PURGE)





