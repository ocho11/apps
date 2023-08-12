from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/ielts_words.csv")


def pick_word():
    global word
    word_of_words = random.choice(data.Word)
    canvas.itemconfig(word, text=word_of_words)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img_card)
canvas.create_text(400, 150, text="Word", font=("Arial", 40, "italic"))
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
