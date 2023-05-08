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


def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}ml')
    print(f'Money: ${profit} in total')


def resource_check(coffee_checked):
    """Checks if there are enough resources to make chosen coffee"""
    for item in coffee_checked:
        if coffee_checked[item] > resources[item]:
            print("Sorry, there is not enough {item} to make you coffee.")
            return False
        else:
            continue
    return True


def process_coins():
    """Calculates inserted money and returns total"""
    print("Please, insert coins:")
    amount_q = int(input("How many quarters: ")) * 0.25
    amount_d = int(input("How many dimes: ")) * 0.1
    amount_n = int(input("How many nickels: ")) * 0.05
    amount_p = int(input("How many pennies: ")) * 0.01
    total = amount_q + amount_d + amount_n + amount_p
    return total


def money_check(drink_cost, money_received):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if drink_cost <= money_received:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} back")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, this is not enough to make coffee")
        return False


def make_coffee(coffee_choice, drink):
    """Deduct the required ingredients from the resources."""
    for item in coffee_choice:
        resources[item] -= coffee_choice[item]
    print(f"Here is your {drink}. Enjoy!")


profit = 0
in_use = True
# coffee = {}

while in_use:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'off':
        print("I am turning off....")
        in_use = False
        # break
    elif user_choice == 'report':
        print_report()
    else:
        if user_choice == 'espresso':
            coffee = MENU['espresso']
        elif user_choice == 'latte':
            coffee = MENU['latte']
        elif user_choice == 'cappuccino':
            coffee = MENU['cappuccino']
        else:
            print("You did not provide correct choice of coffee or other command.")
            continue

        if resource_check(coffee["ingredients"]):
            inserted_amount = process_coins()
            if money_check(coffee["cost"], inserted_amount):
                make_coffee(coffee["ingredients"], user_choice)
            # else:
            # continue

# TODO: 1 Redo if statements to one block (possibly)
# TODO: 2 Cancel global variable Profit in money_check() - return tuple (boolean, profit increase)
