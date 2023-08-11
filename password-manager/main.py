from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# Generate password
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


def write_json(save_data):
    with open("data.json", mode="w") as file:
        json.dump(save_data, file, indent=4)


def save():
    site = input_website.get()
    email = input_email_username.get()
    password = input_password.get()
    info_save_json = {
        site: {
            "email": email,
            "password": password,
        }
    }

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as file:
                    data_from_json = json.load(file)
                    data_from_json.update(info_save_json)
            except FileNotFoundError:
                write_json(info_save_json)
            else:
                write_json(data_from_json)
            finally:
                input_website.delete(0, END)
                input_password.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)

label_web_site = Label(text="Website:")
label_web_site.grid(row=1, column=0)
input_website = Entry(width=35)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
input_email_username = Entry(width=35)
input_email_username.grid(row=2, column=1, columnspan=2)
input_email_username.insert(0, "example@example.example")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)
input_password = Entry(width=21)
input_password.grid(row=3, column=1)

button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
