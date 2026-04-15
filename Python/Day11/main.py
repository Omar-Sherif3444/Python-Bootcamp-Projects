import random
from my_module import logo

print(logo)

def player_loss(user_score, dealer_score):
    if user_score != 21 and dealer_score == 21:
        return True
    else:
        return False


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_score=0
dealer_score=0

user_aces = 0
dealer_aces = 0

choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if choice=="y":


    card=random.choice(cards)
    user_score+=card
    if card==11:
        user_aces+=1

    card=random.choice(cards)
    dealer_score+=card
    if card==11:
        dealer_aces+=1

    print(f"dealer score={dealer_score}")

    card=random.choice(cards)
    user_score+=card
    if card==11:
        user_aces+=1

    card=random.choice(cards)
    dealer_score+=card
    if card==11:
        dealer_aces+=1

    print(f"user score={user_score}")


    while user_score>21 and user_aces>0:
        user_score-=10
        user_aces-=1


    another_card=input("Do you want another card? Type 'y' or 'n':")

    while another_card=="y" and user_score<=21:

        card=random.choice(cards)
        user_score+=card
        if card==11:
            user_aces+=1


        while user_score>21 and user_aces>0:
            user_score-=10
            user_aces-=1

        print(f"user score={user_score}\n ******************************")

        if user_score>21:
            break

        another_card=input("Do you want another card? Type 'y' or 'n':")


    while dealer_score<17:

        card=random.choice(cards)
        dealer_score+=card
        if card==11:
            dealer_aces+=1

        while dealer_score>21 and dealer_aces>0:
            dealer_score-=10
            dealer_aces-=1

    # Result
    if dealer_score > 21:
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("The computer got a bust, you win!")

    elif player_loss(user_score, dealer_score):
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("You lose.")

    elif user_score == 21 and dealer_score != 21:
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("You win!")

    elif user_score > 21:
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("It's a bust, you lose.")

    elif user_score == dealer_score:
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("It's a draw.")

    elif user_score > dealer_score:
        print(f"user score={user_score}")
        print(f"dealer score={dealer_score}")
        print("You win!")

    else:
        print("You lose.")
