from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.yes_img = PhotoImage(file="./images/true.png")
        self.yes_button = Button(image=self.yes_img)
        self.yes_button.grid(row=2, column=0)

        self.no_img = PhotoImage(file="./images/false.png")
        self.no_button = Button(image=self.no_img)
        self.no_button.grid(row=2, column=1)

        self.window.mainloop()
