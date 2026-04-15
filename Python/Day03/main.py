#num=int(input("enter the number"))
#if num%2==0:
    #print("even")
#elif num%2!=0:
       # print("odd")




#print("welcome to pizza deliveries!")
#size=input("what size do you want? L,M OR S")
#pepperoni=input("do you want pepperoni on your pizza? Y or N?")
#extra_cheese=input("do you want cheese on your pizza? Y or N?")

#bill=0

#if size == "L":
    #bill +=25
#elif size == "M":
    #bill +=20
#elif size == "S":
    #bill +=10
#if pepperoni == "Y":
    #if size == "S":
      #bill+=2
    #else:
      #bill+=3
#if extra_cheese == "Y":
    #bill+=1

#print(f"your bill is {bill}")


print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# First choice
go = input("You're at a cross road. Where do you want to go?\n\tType left or right: ").lower()

if go == "left":
    # Second choice
    choice2 = input(
        "You've come to a lake. There is an island in the middle of the lake.\n"
        "Type 'wait' to wait for a boat.\n"
        "Type 'swim' to swim across: "
    ).lower()

    if choice2 == "wait":
        # Third choice
        choice3 = input(
            "You arrive at the island unharmed.\n"
            "There is a house with 3 doors. One red, one yellow and one blue.\n"
            "Which colour do you choose? "
        ).lower()

        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win! 🎉")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")


