##Project: Coffee Shop
# from menu import Menu
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

is_coffee_machine_on = True

#TODO: 7 create a function that checks if coffee ingredients is sufficient to make new coffee if yes, proceed to request for coin else, print "sorry there's no enough whatever"
def is_coffee_enough(request):
    for item in Menu[request]["ingredients"]:
        if Menu[request]["ingredients"][item] > coffee_machine["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

#TODO: 5 create a function that will calculate the total coin input and return the change if money is sufficient and if not, print "Sorry that's not enough money. Money refunded."
def calc_coin(quarter, dime, nickle, penny):
    total_coin = round((quarter * 0.25) + (dime * 0.1) + (nickle * 0.05) + (penny * 0.01),2)
    if total_coin > Menu[request]["cost"]:
        change = round(total_coin - Menu[request]["cost"], 2)
        print(f"${total_coin} is more than enough to make {request}")
        print(f"Here's ${change} in change")
        print(f"Here's your hot {request} ☕. Enjoy!")
        return True
    elif total_coin == Menu[request]["cost"]:
        print(f"${total_coin} is just enough to make {request}")
        print(f"Here's your hot {request} ☕. Enjoy!")
        return True
    else:
        print(f"${total_coin} is not enough to make {request}")
        print(f"${total_coin} has been refunded")
        return False

#TODO: 6 create a function that checks if transaction is successful and deduct recently made coffee ingredients from the initial one and should replace the dictionary
def coffee_ingredient_left(request):
    water = coffee_machine["ingredients"]["water"] - Menu[request]["ingredients"]["water"]
    milk = coffee_machine["ingredients"]["milk"] - Menu[request]["ingredients"]["milk"]
    coffee = coffee_machine["ingredients"]["coffee"] - Menu[request]["ingredients"]["coffee"]
    money = coffee_machine["amount_made"]["money"] + Menu[request]["cost"]
    coffee_machine["ingredients"]["water"] = water
    coffee_machine["ingredients"]["milk"] = milk
    coffee_machine["ingredients"]["coffee"] = coffee
    coffee_machine["amount_made"]["money"] = money

# TODO: 2 create a dictionary that contains coffee_machine ingredients and money
coffee_machine = {
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    },
    "amount_made": {
        "money": 0,
    },
}

#TODO: 8 create a loop that will continue to ask users what they would like
while is_coffee_machine_on == False:

#TODO: 1 ask user what they would like
    request = input("What coffee would you like? (espresso/latte/cappuccino) Or type 'report' to check status ").lower()

# TODO: 3 if input prompt returns report, print the coffee_machine status at that time
    if request == "report":
        print(f"Water: {coffee_machine["ingredients"]["water"]}ml")
        print(f"Milk: {coffee_machine["ingredients"]["milk"]}ml")
        print(f"Coffee: {coffee_machine["ingredients"]["coffee"]}g")
        print(f"Money: ${coffee_machine["amount_made"]["money"]}")
    elif request == "off":
        is_c0ffee_machine_on = True
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        is_coffee_enough(request)
        if is_coffee_enough(request) == False:
            is_c0ffee_machine_on = False
        else:
            print("Please insert your coins.")
            # TODO: 4 if input prompt returns either espresso, latte, cappuccino, print "Please insert your coins" and request for how many quarters, dimes, nickles,and pennies to be deposited
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))

            #function that will calculate the total coin input and return the change
            calc_coin(quarter, dime, nickle, penny)

            #Function that deducts coffee ingredient used and updates coffee_machine dictionary
            if calc_coin(quarter, dime, nickle, penny) == True:
                coffee_ingredient_left(request)