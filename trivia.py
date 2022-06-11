import json
from tkinter import *
from tkinter import ttk
import winsound
import random
from decimal import *


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
        self.question = Label(root, text="", width=80, bg="black", fg="yellow", font=("Helvetica", 32, "bold"), wraplength=780)
        self.question_number = 0
        self.question_number_display = 0
        self.score_label = Label()
        self.song_name_label = Label(root, text="Song Name:  " + music_dictionary[list_music[self.music_count]], width=60, bg="black", fg="lightblue", font=("Helvetica", 16, "bold"), anchor="w")
        self.song_name_label.place(relx=0, rely=0.95)
        self.answer_button_1 = Button()
        self.answer_button_2 = Button()
        self.answer_button_3 = Button()
        self.answer_button_4 = Button()
        self.questions = []
        self.answers = []
        self.choices = []
        self.result_label = Label()
        self.result_label_percent = Label()
        self.questions_left_label = Label()
        self.time_label = Label(root, text="", width=12, bg="black", fg="red", font=("Helvetica", 24, "bold"))
        self.time_left = 0
        self.after_id = None

    def buttons(self):
        quit_button = Button(root, text="Quit", command=root.destroy, width=12, bg="darkred", fg="white", font=("Helvetica", 16, "bold"))
        quit_button.pack(side="bottom", anchor="se")

        stop_music_button = Button(root, text="Stop Music", command=stop_music, width=12, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        stop_music_button.pack(side="bottom", anchor="se")

        change_music_button = Button(root, text="Change Music", command=self.change_music, width=12, bg="purple", fg="white", font=("Helvetica", 16, "bold"))
        change_music_button.pack(side="bottom", anchor="se")

        toggle_window_button = Button(root, text="Toggle Window", command=self.is_fullscreen_command, width=12, bg="brown", fg="white", font=("Helvetica", 16, "bold"))
        toggle_window_button.pack(side="bottom", anchor="se")

        start_button = Button(root, text="Start", command=lambda: [self.start_trivia(), start_button.destroy()], width=12, bg="#e4000f", fg="white", font=("Helvetica", 16, "bold"))
        start_button.place(relx=0.5, rely=0.5, anchor="center")

    def countdown(self, time):
        self.time_left = time
        if self.time_left < 0:
            self.time_label.configure(text="Timer: 0")
            self.after_id = None
            self.countdown(5)
            self.update_question_prompt()
        else:
            self.time_label.configure(text="Timer: " + "%d" % self.time_left)
            self.time_left -= 1
            self.after_id = root.after(1000, self.countdown, self.time_left)

    def change_music(self):
        self.music_count += 1
        if self.music_count == len(list_music):
            self.music_count = 0
        self.music_name = list_music[self.music_count]
        music_string = 'Music/' + self.music_name + '.wav'
        winsound.PlaySound(music_string, winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        self.update_song_name()

    def is_fullscreen_command(self):
        self.is_fullscreen = not self.is_fullscreen
        root.attributes('-fullscreen', self.is_fullscreen)

    def start_trivia(self):
        self.answer_buttons()
        self.score_label = Label(root, text="Score: 0", width=20, bg="black", fg="lightgreen", font=("Helvetica", 16, "bold"))
        self.score_label.place(relx=0.5, rely=0.75, anchor="center")
        self.randomize_qca()
        self.question.place(relx=0.5, rely=0.3, anchor="center")
        self.question_prompt()
        self.question_number_display = len(self.questions)
        self.questions_left_label = Label(root, text="Questions Unanswered: " + str(self.question_number_display), width=24, bg="black", fg="pink", font=("Helvetica", 16, "bold"))
        self.questions_left_label.place(relx=0.5, rely=0.8, anchor="center")
        self.time_label.place(relx=0.5, rely=0.45, anchor="center")
        self.countdown(5)

    def answer_buttons(self):
        self.answer_button_1 = Button(root, text="Q1", command=self.answer_1, width=20, bg="#101010", fg="white", font=("Helvetica", 16, "bold"))
        self.answer_button_1.place(relx=0.2, rely=0.6, anchor="center")

        self.answer_button_2 = Button(root, text="Q2", command=self.answer_2, width=20, bg="#101010", fg="white", font=("Helvetica", 16, "bold"))
        self.answer_button_2.place(relx=0.4, rely=0.6, anchor="center")

        self.answer_button_3 = Button(root, text="Q3", command=self.answer_3, width=20, bg="#101010", fg="white", font=("Helvetica", 16, "bold"))
        self.answer_button_3.place(relx=0.6, rely=0.6, anchor="center")

        self.answer_button_4 = Button(root, text="Q4", command=self.answer_4, width=20, bg="#101010", fg="white", font=("Helvetica", 16, "bold"))
        self.answer_button_4.place(relx=0.8, rely=0.6, anchor="center")

    def answer_1(self):
        if self.answer_button_1['text'] == self.answers[self.question_number]:
            self.score += 1
            self.update_score()
        self.update_question_prompt()

    def answer_2(self):
        if self.answer_button_2['text'] == self.answers[self.question_number]:
            self.score += 1
            self.update_score()
        self.update_question_prompt()

    def answer_3(self):
        if self.answer_button_3['text'] == self.answers[self.question_number]:
            self.score += 1
            self.update_score()
        self.update_question_prompt()

    def answer_4(self):
        if self.answer_button_4['text'] == self.answers[self.question_number]:
            self.score += 1
            self.update_score()
        self.update_question_prompt()

    def update_score(self):
        self.score_label.configure(text="Score: " + str(self.score))

    def update_song_name(self):
        self.song_name_label.configure(text="Song Name:  " + music_dictionary[list_music[self.music_count]])

    def update_question_prompt(self):
        self.question_number += 1
        self.question_number_display -= 1
        self.question_prompt()

    def question_prompt(self):
        if self.question_number == len(self.questions):
            self.result()
        else:
            if self.after_id is not None:
                root.after_cancel(self.after_id)
                self.countdown(5)

            self.question.configure(text="")
            self.question.configure(text=self.questions[self.question_number])
            self.questions_left_label.configure(text="Questions Unanswered: " + str(self.question_number_display))
            answer_list = [1, 2, 3, 4]
            for choice in self.choices[self.question_number]:
                rand_answer_button = random.choice(answer_list)
                if rand_answer_button == 1:
                    self.answer_button_1.configure(text=choice)
                elif rand_answer_button == 2:
                    self.answer_button_2.configure(text=choice)
                elif rand_answer_button == 3:
                    self.answer_button_3.configure(text=choice)
                else:
                    self.answer_button_4.configure(text=choice)
                answer_list.remove(rand_answer_button)

    def randomize_qca(self):
        self.questions = section['question']
        self.choices = section['choices']
        self.answers = section['answer']
        zip_qca = zip(self.questions, self.choices, self.answers)
        list_qca = list(zip_qca)
        random.shuffle(list_qca)
        self.questions, self.choices, self.answers = zip(*list_qca)

    def result(self):
        root.after_cancel(self.after_id)
        self.after_id = None
        self.time_left = 0
        self.time_label.configure(text="")
        self.answer_button_1.destroy()
        self.answer_button_2.destroy()
        self.answer_button_3.destroy()
        self.answer_button_4.destroy()
        self.question.configure(text="")
        self.score_label.configure(text="")
        self.questions_left_label.configure(text="")
        self.song_name_label.configure(text="")
        stop_music()
        self.result_label = Label(root, text="Your final score was " + str(self.score) + "/" + str(len(self.questions)) + "!", width=30, bg="black", fg="white", font=("Helvetica", 32, "bold"))
        self.result_label.place(relx=0.5, rely=0.5, anchor="center")
        result_percent = str(100 * round(Decimal(self.score)/Decimal(len(self.questions)), 2))
        result_percent_split = result_percent.split(".")
        self.result_label_percent = Label(root, text="(" + result_percent_split[0] + "%)", width=30, bg="black", fg="white", font=("Helvetica", 16, "bold"))
        self.result_label_percent.place(relx=0.5, rely=0.55, anchor="center")
        replay_button = Button(root, text="Replay", command=lambda: [self.replay(), replay_button.destroy()], width=12, bg="#e40000", fg="white", font=("Helvetica", 16, "bold"))
        replay_button.place(relx=0.5, rely=0.65, anchor="center")

    def replay(self):
        self.randomize_qca()
        self.score = 0
        self.question_number = 0
        self.music_count = 0
        self.result_label.configure(text="")
        self.result_label_percent.configure(text="")
        self.start_trivia()
        random.shuffle(list_music)
        winsound.PlaySound('Music/' + list_music[0] + '.wav', winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
        self.update_song_name()


trivia = Trivia()
root.mainloop()
winsound.PlaySound(None, winsound.SND_PURGE)





