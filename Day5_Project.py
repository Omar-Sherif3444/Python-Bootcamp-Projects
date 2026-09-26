import random
#fruits=["apple","peach","mango"]
#for fruit in fruits:
#print(fruit)

#student_scores=[103,123,146,147,189,150,145,123,109,107,176,167,199]

#max_score=0

#for score in student_scores:
    #if score>max_score:
        #max_score=score

#print("The highest score in the list is",max_score)

#for number in range(1,10): #to print numbers from 1 to 9
#for number in range(1,11,3): #to print numbers from 1 to 10 and add 3 every time(1,4,7,10)

#sum=0
#for number in range(1,101):
    #sum+=number

#print(sum)

#for number in range(1,101):
    #if number%3==0 and number%5==0:
        #print("FizzBuzz")
    #elif number%3==0:
        #print("Fizz")
    #elif number%5==0:
        #print("Buzz")
    #elif number%3==0 and number%5==0:
       # print("FizzBuzz")
    #else:
        #print(number)

letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
digits = ['0','1','2','3','4','5','6','7','8','9']
password_symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','=','+','[',']','{','}','|',
    ';',':',"'",'"',',','<','>','.','/','?','`','~','\\'
]
print ("welcome to smoozie password generator!")
num_of_letters=int(input("how many letters do you want in the password\n"))
num_of_digits=int(input("how many digits do you want in the password\n"))
num_of_symbols=int(input("how many symbols do you want in the password\n"))

password_list=[]
for char in range(0,num_of_letters):
    password_list.append(random.choice(letters))
for char in range(0,num_of_digits):
    password_list.append(random.choice(digits))
for char in range(0, num_of_symbols):
    password_list.append(random.choice(password_symbols))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char

print(f"your password is {password}")


