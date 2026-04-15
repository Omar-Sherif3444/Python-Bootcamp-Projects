#print(5//3) just print the int and clear the decimal part
#print (2**3) this means 2 power 3 =8
#we can use round function to round up or down decimal number - round(number,ndigits) cut the number on ndigits value
#final project
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

bill_after_tip = total_bill + (tip_percent / 100) * total_bill
each_person = bill_after_tip / people
final_amount=round(each_person,2)
print(f"Each person should pay: {final_amount} $")







