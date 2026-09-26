from replit import clear
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
#     "Variable": "A container for storing data values."
# }
# print(programming_dictionary["Bug"])
# programming_dictionary["Bug"]="error in your system"
# print(programming_dictionary)
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#*********************************************************
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# # Create an empty dictionary
# student_grades = {}
#
# # Loop through the student_scores dictionary
# for student, score in student_scores.items():
#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
# print(student_grades)
# travel_Log={
#     "France":["lille","Paris"]
# }
# print(travel_Log["France"][1])
bidP = {}

def add_persons(name, bid):
    bidP[name] = bid


continue_bid = True

while continue_bid:
    print("Welcome to the private bidding auction")
    name = input("What is your name?: ")
    bid = float(input("How much would you like to bid?: $"))

    add_persons(name, bid)

    should_continue = input(
        "Are there any other bidders for this auction? Type 'yes' or 'no'.\n"
    ).lower()


    if should_continue == "yes":
        print("\n"*40)

    elif should_continue == "no":
        continue_bid = False


highest_bidder = 0
winner = ""

for e in bidP:
    if bidP[e] > highest_bidder:
        highest_bidder = bidP[e]
        winner = e

print(f"The highest bidder is {winner} with a ${highest_bidder}")
print("Thank you for your participation.")
