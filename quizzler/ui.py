from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(
            150,
            125,
            text="question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        yes_img = PhotoImage(file="./images/true.png")
        self.yes_button = Button(image=yes_img, highlightthickness=0)
        self.yes_button.grid(row=2, column=0)

        no_img = PhotoImage(file="./images/false.png")
        self.no_button = Button(image=no_img, highlightthickness=0)
        self.no_button.grid(row=2, column=1)

        self.window.mainloop()
