import random
from my_module import logo2
print(logo2)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty .type 'easy' for easy or 'hard' for hard: ").lower()
won = False
number=random.randint(1,100)
if difficulty == "easy":
    attempts = 10
    print("you have 10 attempts to guess the number.")
    g1 =int( input("Guess the number: "))
    if g1==number:
     print("You guessed the number.")
     won=True
    elif g1!=number:
        attempts=attempts-1
        while attempts>0:
            gg= int(input("guess again"))
            if gg == number:
                print("You guessed the number.")
                won = True
                break
            elif gg > number:
                print("Too high guess")
                attempts = attempts - 1
                print(f"Remaining Attempts {attempts}")
            elif gg < number:
                print("Too low guess")
                attempts = attempts - 1
                print(f"Remaining Attempts {attempts}")

    if not won:
        print(f"you have lost , the correct number was{number}")
elif difficulty == "hard":
    attempts = 5
    print("you have 5 attempts to guess the number.")
    g3 = int(input("Guess the number: "))
    print(f"Remaining Attempts {attempts}")
    if g3 == number:
        print("You guessed the number.")
        won=True
    elif g3 != number:
        attempts = attempts - 1
        while attempts > 0:
            gg = int(input("guess again"))
            if gg == number:
                print("You guessed the number.")
                won=True
                break
            elif gg > number:
                print("Too high guess")
                attempts = attempts - 1
                print(f"Remaining Attempts {attempts}")
            elif gg < number:
                print("Too low guess")
                attempts = attempts - 1
                print(f"Remaining Attempts {attempts}")
    if not won:
        print(f"you have lost , the correct number was{number}")