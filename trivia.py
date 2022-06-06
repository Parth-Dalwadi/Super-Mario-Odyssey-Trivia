import json
from tkinter import *
from tkinter import ttk
import winsound
import random


# Music
with open('musicNames.json') as music_file:
    music_obj = json.load(music_file)


music_names = music_obj['names']
list_music = list(music_names)
random.shuffle(list_music)


winsound.PlaySound('Music/' + list_music[0] + '.wav', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)


def stop_music():
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
root.attributes('-fullscreen', True)
root.title("Super Mario Odyssey Trivia")
root.configure(background="black")
title = Label(root, text="Super Mario Odyssey Trivia", width=width, foreground="white", background="#e4000f", font=("Helvetica", 24, "bold"))
title.pack(side="top")


class Trivia:
    def __init__(self):
        self.buttons()
        self.music_count = 0
        self.music_name = ''
        self.is_fullscreen = True
        self.score = 0
        self.question = ""
        self.question_number = 1

    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")

        stop_music_button = Button(root, text="Stop Music", command=stop_music, width=12, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        stop_music_button.pack(side="bottom", anchor="se")

        change_music_button = Button(root, text="Change Music", command=self.change_music, width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
        change_music_button.pack(side="bottom", anchor="se")

        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen, width=12, bg="brown", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")

        start_button = Button(root, text="Start", width=12, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        start_button.place(relx=0.5, rely=0.5, anchor="center")

    def change_music(self):
        self.music_count += 1
        if self.music_count == len(list_music):
            self.music_count = 0
        self.music_name = list_music[self.music_count]
        music_string = 'Music/' + self.music_name + '.wav'
        winsound.PlaySound(music_string, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)

    def is_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        root.attributes('-fullscreen', self.is_fullscreen)


trivia = Trivia()
root.mainloop()
winsound.PlaySound(None, winsound.SND_PURGE)





