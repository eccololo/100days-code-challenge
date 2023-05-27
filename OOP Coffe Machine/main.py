from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep


def print_menu():
    print("Welcome.")
    print("*" * 30)
    print("Menu:")
    print("1 - Print Report.")
    print("2 - Order Coffee.")
    print("3 - Print Menu again.")
    print("4 - Quit.")


def clear_console():
    print('\n' * 150)


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print_menu()
while True:
    choose = int(input("What is your option?: "))
    if choose == 1:
        coffee_maker.report()
        money_machine.report()
    elif choose == 2:
        print("What kind of coffee do you want to order?")
        print(menu.get_items()[:-1])
        coffee_choice = input(": ").lower()
        order = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(order):
            payment_passed = money_machine.make_payment(order.cost)
            if payment_passed:
                coffee_maker.make_coffee(order)
                sleep(4)
                clear_console()
                print_menu()
            else:
                print("Goodbye!")
                break
        else:
            print("Goodbye!")
            break
    elif choose == 3:
        clear_console()
        print_menu()
    elif choose == 4:
        print("Goodbye!")
        break
