import random
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
HANGMANPICS = HANGMANPICS[::-1]
word_list=('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
chosen_word=random.choice(word_list)
correct_letters=[]
game_over=False
lives=6
while not game_over :
    print(f"****************** "+str(lives)+"/6 remain *******************")
    guess = input("Enter your guess: \n").lower()
    if guess in correct_letters:
        print(f"you've already guessed{guess}")
    place_holder = ""
    for letter in chosen_word:
        if letter == guess:
            place_holder+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            place_holder += letter
        else:
            place_holder+="_"
    print(place_holder)

    if guess not in correct_letters:
        print("you guessed "+guess+",that's not in the word,you lost a life")
        lives-=1
        if lives ==0 :
            game_over=True
            print("you lose")

    if "_" not in place_holder:
        game_over=True
        print("🎉 You win!")


    print(HANGMANPICS[lives])