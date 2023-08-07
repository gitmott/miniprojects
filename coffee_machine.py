# TODO Everything

# print report, or order if required

def begin_order():
    order = input("What would you like? (espresso, latte, cappuccino)")
    if order.lower() == "report":
        print("report")
    elif order.lower() == "espresso":
        print("Espresso")
    elif order.lower() == "latte":
        print("latte")
    elif order.lower() == "cappuccino":
        print("cappuccino")
    else:
        print("Incorrect instructions. Please re-enter and check for spelling mistakes. ")


ongoing = True
while ongoing:
    begin_order()






# check resources are sufficient
# process coins/payment/change and make sure it is the right amount
#check transaction is successful
# If all else passes, make the coffee and deduct the resources from the running total




# comment
# requirements
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

