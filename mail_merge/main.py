PLACEHOLDER = "[name]"
with open("./Input/Letters/starting_letter.txt") as letter:
    content_of_invitation = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.read()
    names_list = invited_names.splitlines()
    for name in names_list:
        new_content = content_of_invitation.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as invitation:
            invitation.write(new_content)
