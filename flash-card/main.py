import time
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WORD = "Word"
MEANING = "Meaning"

data = pandas.read_csv("./data/ielts_words.csv")
word_of_words = None
words_dictionary = dict(zip(data.Word, data.Meaning))


def pick_word():
    global word
    global word_of_words
    word_of_words = random.choice(data.Word)
    canvas.itemconfig(title, text=WORD, fill="Black")
    canvas.itemconfig(word, text=word_of_words, fill="Black")
    canvas.itemconfig(card_background, image=front_img_card)
    window.after(3000, func=display_translation)


def display_translation():
    global card_background
    global back_img_card
    global title
    global word_of_words
    global word

    canvas.itemconfig(card_background, image=back_img_card)
    canvas.itemconfig(title, text=MEANING, fill="White")
    canvas.itemconfig(word, text=words_dictionary[word_of_words], fill="White")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=display_translation)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img_card = PhotoImage(file="./images/card_front.png")
back_img_card = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_img_card)
title = canvas.create_text(400, 150, text=WORD, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0, command=pick_word)
incorrect_button.grid(row=1, column=0)

correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=pick_word)
correct_button.grid(row=1, column=1)

pick_word()

window.mainloop()
