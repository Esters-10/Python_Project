from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# menu_item = MenuItem()
menu = Menu()

is_coffee_machine_on = True

#TODO: 1 ask user what they would like
while is_coffee_machine_on:
    choice = menu.get_items()
    request = input(f"What coffee would you like? ({choice})  Or type 'report' to check status ").lower()
    if request == "report":
        coffee_maker.report()
        money_machine.report()

    elif request == "off":
            is_coffee_machine_on = False
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)






