import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.quiz = quiz_brain
        self.canvas = Canvas(width=300, height=250)
        self.quiz_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        yes_img = PhotoImage(file="./images/true.png")
        self.yes_button = Button(image=yes_img, highlightthickness=0, command=self.yes_button_clicked)
        self.yes_button.grid(row=2, column=0)

        no_img = PhotoImage(file="./images/false.png")
        self.no_button = Button(image=no_img, highlightthickness=0, command=self.no_button_clicked)
        self.no_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_text, text=question_text)

    def yes_button_clicked(self):
        self.give_answer_by_colour(self.quiz.check_answer("True"))

    def no_button_clicked(self):
        self.give_answer_by_colour(self.quiz.check_answer("False"))

    def give_answer_by_colour(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question())
