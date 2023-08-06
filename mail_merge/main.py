with open("./Input/Letters/starting_letter.txt") as letter:
    content_of_invitation = letter.read()


def save_mail(mail_name, content_invitation):
    with open(f"./Output/ReadyToSend/{mail_name}.txt", mode="w") as invitation:
        invitation.write(content_invitation)


with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.read()
    names_list = invited_names.splitlines()
    for name in names_list:
        content_of_invitation.replace("[name]", name)
        save_mail(name, content_of_invitation)
