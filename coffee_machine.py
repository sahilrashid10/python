menu = {
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

def process_coins():
    quarters = int(input("quarters? "))
    dimes = int(input("dimes? "))
    nickles = int(input("nickles? "))
    pennies = int(input("pennies? "))
    c = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return c

def calculate_change(order, coins):
    required_coins = menu[order]["cost"]
    change = coins - required_coins
    if change >= 0:
        print(f"Enjoy your {order} ☕❤️")
        print(f"Here is your change: ${change:.2f}")
        return True
    else:
        print("Not enough coins, money has been refunded")
        return False


def process_resources(order_resources):
    for item in order_resources:
        resources[item] = resources[item] - order_resources[item]

def check(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            return f"Sorry ,there is not enough {item} "
    return True



def coffee_machine():
    #1.take order
    money = 0
    #2. check if employee wants to continue with the machine or not
    #2. check if he wants to see a report
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == 'off':
            return
        elif order == 'report':
            print(f"WATER: {resources["water"]}")
            print(f"COFFEE:{resources["coffee"]}")
            print(f"MILK:  {resources["milk"]}")
            print(f"MONEY: {money}")
            #check if order can be processed or not
        else:
            drink = menu[order]
            print("Please enter coin's: ")
            print(check(drink["ingredients"]))
            coins = process_coins()
            change = calculate_change(order, coins)

            if change:
                money += drink["cost"]
                process_resources(drink["ingredients"])

coffee_machine()
