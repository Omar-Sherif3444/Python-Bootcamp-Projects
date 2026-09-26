# def format_name(f_name,l_name):
#     ff_name=f_name.title()
#     fl_name=l_name.title()
#     return ff_name,fl_name
#
# print(format_name('OmAr','sherIF'))

# def function1(text):
#     return text+text
# def function2(text):
#     return text.title()
#
# output=function2(function1("hello"))
# print(output)

# def format_name(f_name,l_name):
#      if f_name=="" or l_name=="":
#          return "You did not provide valid input"
#
#      ff_name=f_name.title()
#      fl_name=l_name.title()
#      return f"Result:{ff_name} {fl_name}"
# print(format_name(input("What is your first name?"),input("What is your last name?")))
def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():

    num1 = float(input("What is the first number? "))
    operation = input("pick an operation:\n*\n+\n-\n/")
    num2 = float(input("What is the next number? "))

    continu = True

    while continu:

        if operation == "*":
            result = multiplication(num1, num2)
        elif operation == "+":
            result = add_numbers(num1, num2)
        elif operation == "-":
            result = subtract_numbers(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)

        print(result)

        answer = input(
            f"do you need to continue with {result}? Type 'yes' or 'no'.\n"
        ).lower()

        if answer == "yes":
            num1 = result
            operation = input("pick an operation:\n*\n+\n-\n/")
            num2 = float(input("What is the next number? "))

        else:
            continu = False
            print("\n"*20)

