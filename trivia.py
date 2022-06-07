import json
from tkinter import *
from tkinter import ttk
import winsound
import random


# Music
with open('musicNames.json') as music_file:
    music_section = json.load(music_file)


music_names = music_section['names']
full_names = music_section['full_names']
list_music = list(music_names)
list_full_music_names = list(full_names)

music_dictionary = {}
dictionary_count = 0
for music in list_music:
    music_dictionary.update({music: list_full_music_names[dictionary_count]})
    dictionary_count += 1

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
root.iconbitmap("Images/cappy.ico")
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
        self.question_number = 0
        self.question_number_display = 1
        self.num_of_questions = len(questions)
        self.score_label = Label()
        self.song_name_label = Label(root, text="Song Name:  " + music_dictionary[list_music[self.music_count]], width=60, bg="black", fg="white", font=("Helvetica", 16, "bold"), anchor="w")
        self.song_name_label.place(relx=0, rely=0.95)

    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")

        stop_music_button = Button(root, text="Stop Music", command=stop_music, width=12, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        stop_music_button.pack(side="bottom", anchor="se")

        change_music_button = Button(root, text="Change Music", command=self.change_music, width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
        change_music_button.pack(side="bottom", anchor="se")

        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen, width=12, bg="brown", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")

        start_button = Button(root, text="Start", command=lambda: [self.start_trivia(), start_button.destroy()], width=12, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        start_button.place(relx=0.5, rely=0.5, anchor="center")

    def change_music(self):
        self.music_count += 1
        if self.music_count == len(list_music):
            self.music_count = 0
        self.music_name = list_music[self.music_count]
        music_string = 'Music/' + self.music_name + '.wav'
        winsound.PlaySound(music_string, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        self.update_song_name()

    def is_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        root.attributes('-fullscreen', self.is_fullscreen)

    def start_trivia(self):
        self.answer_buttons()
        self.score_label = Label(root, text="Score: 0", width=20, bg="black", fg="white", font=("Helvetica", 16, "bold"))
        self.score_label.place(relx=0.5, rely=0.75, anchor="center")

    def answer_buttons(self):
        answer_button_1 = Button(root, text="Q1", command=self.answer, width=20, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        answer_button_1.place(relx=0.2, rely=0.6, anchor="center")

        answer_button_2 = Button(root, text="Q2", command=lambda: answer_button_2.destroy(), width=20, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        answer_button_2.place(relx=0.4, rely=0.6, anchor="center")

        answer_button_3 = Button(root, text="Q3", command=lambda: answer_button_3.destroy(), width=20, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        answer_button_3.place(relx=0.6, rely=0.6, anchor="center")

        answer_button_4 = Button(root, text="Q4", command=lambda: answer_button_4.destroy(), width=20, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        answer_button_4.place(relx=0.8, rely=0.6, anchor="center")

    def answer(self):
        self.score += 1
        self.update_score()
        print(self.score)

    def update_score(self):
        self.score_label.configure(text="Score: " + str(self.score))

    def update_song_name(self):
        self.song_name_label.configure(text="Song Name:  " + music_dictionary[list_music[self.music_count]])


trivia = Trivia()
root.mainloop()
winsound.PlaySound(None, winsound.SND_PURGE)





