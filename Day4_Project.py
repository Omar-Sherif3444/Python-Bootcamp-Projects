import random
#random_int=random.randint(1,100) #return int num between 1 and 100
#print(random_int)

#import my_module
#print(my_module.my_num)

#rand1=random.random() *10 not include 10  #return num between 0 and 1
#print(rand1)

#random_float=random.uniform(1,100)
#print(random_float)

#num1=random.randint(0,1)
#if num1==1:
    #print("Heads")
#elif num1==0:
    #print("Tails")

friends=["ALI","WILSON","MARK","SMITH","AHMED"]
#1st option
#Who_will_pay=random.choice(friends)
#print(Who_will_pay)
#2nd option
#random_index=random.randint(0,4)
#print(friends[random_index])

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
user_choice=int(input("what do you choose type 0 for rock,1 for paper or 2 for scissors?\n"))
computer_choice=random.randint(0,2)
if user_choice==computer_choice:
    print("Draw")
elif user_choice==0 and computer_choice==1:
    print("your choice :" +rock)
    print("computer choice :"+paper)
    print("You Lose!")
elif user_choice==1 and computer_choice==0:
    print("your choice :" +paper)
    print("computer choice :"+rock)
    print("You Win!")
elif user_choice==1 and computer_choice==2:
    print("your choice :" + paper)
    print("computer choice :" + Scissors)
    print("You Lose!")
elif user_choice==2 and computer_choice==0:
    print("your choice :" + Scissors)
    print("computer choice :" + rock)
    print("You Lose!")
elif user_choice==2 and computer_choice==1:
    print("your choice :" + Scissors)
    print("computer choice :" + paper)
    print("You Win!")
elif user_choice >= 3 or user_choice<0:
    print("invalid choice")