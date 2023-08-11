import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets_and_NATO = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    entered_word = input("Enter a word: ").upper()
    try:
        entered_letters_with_NATO = [alphabets_and_NATO[letter] for letter in entered_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(entered_letters_with_NATO)


generate_phonetic()
