from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
menu = Menu()
money = MoneyMachine()
coffee_maker = CoffeeMaker()

while machine_is_on:

    order_name = input(f"Name your order from the available items in the list {menu.get_items()} : ")

    if order_name == "report":
        coffee_maker.report()
        money.report()

    elif order_name == "off":
        machine_is_on = False

    else:
        print(f"You have requested for {order_name}")
        chosen_item = menu.find_drink(order_name)
        print(chosen_item)
        resource_check = coffee_maker.is_resource_sufficient(chosen_item)

        if resource_check is True:
            amount = money.make_payment(chosen_item.cost)
            if amount is True:
                coffee_maker.make_coffee(chosen_item)