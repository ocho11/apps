import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
entered_word = input("Enter a word: ").upper()
print(entered_word)

alphabets_and_NATO = {row.letter: row.code for (index, row) in data.iterrows()}
entered_letters_with_NATO = [alphabets_and_NATO[letter] for letter in entered_word]
print(entered_letters_with_NATO)