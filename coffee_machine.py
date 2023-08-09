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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins")
    total = float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.10
    total += float(input("How many nickels?: ")) * 0.05
    total += float(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_recieved, drink_cost):
    """Return true when payment accepted, False when money insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your ${change} change.")
        global profit
        profit += drink_cost 
        return True
    else:
        print("Sorry that's not enough money")
        return False


def make_coffee(drink_name, order_ingredient):
    """Deduct coffee ingredients from total """
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {order}\n Enjoy! :)")


is_on = True

while is_on:
    order = input("What would you like? (espresso, latte, cappuccino): ")
    if order.lower() == "off":
        is_on = False
    elif order.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
