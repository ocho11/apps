BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR)
front_img_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_img_card)
canvas.grid(row=0, rowspan=4, column=0, columnspan=3)

label_of_title = Label(text="Title", font=("Arial", 32), bg="White")
label_of_title.grid(row=1, column=1)

label_of_word = Label(text="Word", font=("Arial", 45, "bold"), bg="White")
label_of_word.grid(row=2, column=1)

incorrect_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_img, highlightthickness=0)
incorrect_button.grid(row=4, column=0)

correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0)
correct_button.grid(row=4, column=2)

window.mainloop()
