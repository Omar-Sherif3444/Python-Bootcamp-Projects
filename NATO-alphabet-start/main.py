
import pandas
nato=pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
dictt={row.letter:row.code for (index,row) in nato.iterrows()}
# print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
LL=True
while LL:
    words=input("Enter a word:").upper()
    try:
        kk=[dictt[letter] for letter  in words ]
    except KeyError:
        print("Sorry,only letters in the alphabet please.")
    else:
        print(kk)
        LL=False
