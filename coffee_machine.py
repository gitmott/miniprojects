# TODO Everything

# print report, or order if required
order = input("What would you like? (espresso, latte, cappuccino)")
# check resources are sufficient
# process coins/payment/change and make sure it is the right amount
#check transaction is successful
# If all else passes, make the coffee and deduct the resources from the running total

# if order.lower() == "report":
# elif order.lower() == "espresso":
# elif order.lower() == "latte":
# elif order.lower() == "cappuccino":
# else:
#     print("Incorrect instructions. Please re-enter and check for spelling mistakes. ")


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

