import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def report():
    print(f"Water :{resources['water']} ml")
    print(f"Milk :{resources['milk']} ml")
    print(f"Coffee :{resources['coffee']} ml")
    print(f"Money :{money['value']} $")
def process_coins(quarter, dime, nickle, penny):
    quarter *= 0.25
    dime *= 0.10
    nickle *= 0.05
    penny *= 0.01
    total = quarter + dime + nickle + penny
    return total
def check_resources(coffee_choice):
    enough = True
    if MENU[coffee_choice]['ingredients']['water'] > resources['water']:
        print(f"There isn't enough water for a {coffee_choice}.")
        enough = False
    if MENU[coffee_choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There isn't enough coffee for a {coffee_choice}.")
        enough = False
    if coffee_choice != 'espresso':
        if MENU[coffee_choice]['ingredients']['milk'] > resources['milk']:
            print(f"There isn't enough milk for a {coffee_choice}.")
            enough = False
    return enough
machine_on = True
while machine_on:
    choice=input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if choice=="espresso":
        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = process_coins(quarters, dimes, nickles, pennies)
        if check_resources('espresso'):
            if total >= MENU['espresso']['cost']:
                money['value'] += MENU['espresso']['cost']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                change = total - MENU['espresso']['cost']
                print(f"Your change is: {round(change, 2)}$")
                print("Your espresso is ready ")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif choice=="latte":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = process_coins(quarters, dimes, nickles, pennies)
        if check_resources('latte'):
            if total >= MENU['latte']['cost']:
                money['value'] += MENU['latte']['cost']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                resources['milk'] -= MENU[choice]['ingredients']['milk']
                change = total - MENU['latte']['cost']
                print(f"Your change is: {round(change, 2)}$")
                print("Your latte is ready ")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif choice=="cappuccino":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = process_coins(quarters, dimes, nickles, pennies)
        if check_resources('cappuccino'):
            if total >= MENU['cappuccino']['cost']:
                money['value'] += MENU['cappuccino']['cost']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                resources['milk'] -= MENU[choice]['ingredients']['milk']
                change = total - MENU['cappuccino']['cost']
                print(f"Your change is: {round(change, 2)}$")
                print("Your cappuccino is ready ")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif choice == "turn off":
        print("Turning Off")
        machine_on=False
    elif choice=="report":
        report()
    else:
        print("invalid input")
    input("Press Enter to continue...")
    clear_screen()