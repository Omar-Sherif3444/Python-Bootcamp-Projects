from my_module import logo3
from my_module import vs
from Day14_Data import data
import random
from replit import clear

def profile():
    number = random.randint(0, 49)
    name = data[number]['name']
    follower_count = data[number]['follower_count']
    description = data[number]['description']
    country = data[number]['country']
    full = f"{name}, {description}, from {country}"
    return full, follower_count
play_game = True
while play_game:
    profile_a, followers_a = profile()
    profile_b, followers_b = profile()
    score = 0
    correct = True
    while correct:
        clear()
        print(logo3)
        if score > 0:
            print(f"Correct! Your current score is: {score}.")
        print(f"Compare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")
        choice = input("\nWho has more followers? Type 'a' or 'b': ").lower()
        if choice == 'a' and followers_a >= followers_b:
            score += 1
            profile_b, followers_b = profile()
        elif choice == 'b' and followers_b >= followers_a:
            score += 1
            profile_a, followers_a = profile()
        else:
            print(f"\nIncorrect! Final score: {score}")
            correct = False
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        play_game = False
        print("\nThanks for playing ")
