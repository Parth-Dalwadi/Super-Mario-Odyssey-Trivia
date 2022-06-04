import json
from tkinter import *
from tkinter import ttk
import winsound
import random


# Music
winsound.PlaySound('Music/steamGardens.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


def stop_music():
    winsound.PlaySound(None, winsound.SND_ASYNC)


def change_music():
    winsound.PlaySound(None, winsound.SND_ASYNC)


# Trivia Game
with open('triviaQ&A.json') as file:
    section = json.load(file)

questions = section['question']
choices = section['choices']
answers = section['answer']
zipQCA = zip(questions, choices, answers)
listQCA = list(zipQCA)
random.shuffle(listQCA)
questions, choices, answers = zip(*listQCA)

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
ttk.Button(frm, text="Stop Music", command=stop_music).grid(column=2, row=0)


class Trivia:
    def __init__(self):
        self


root.mainloop()
winsound.PlaySound(None, winsound.SND_PURGE)





