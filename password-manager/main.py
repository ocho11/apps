from tkinter import *


def save():
    site_name = input_website.get()
    password = input_password.get()

    input_website.delete(0, END)
    input_password.delete(0, END)
    with open("data.txt", mode="a") as file:
        file.write(f"{site_name}\n{password}\n\n")


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

button_generate_password = Button(text="Generate Password")
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
