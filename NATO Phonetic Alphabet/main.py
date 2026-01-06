import pandas
#TODO 1. Create a dictionary in this format:
NATO_alphabet_phonetics_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_alphabet_phonetics = {alphabet.letter:alphabet.code for (word, alphabet) in NATO_alphabet_phonetics_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def convert_to_nato_phonetics():
    user_input = input("Enter the word you want to encode: ").upper()
    decoded_word_list = [NATO_alphabet_phonetics[value] if value in NATO_alphabet_phonetics else "Unknown Character" for value in user_input]
    print(decoded_word_list)

while True:
    convert_to_nato_phonetics()
    go_again = input("Want to use it again? Type y or n: ")
    if go_again!= "y":
        break