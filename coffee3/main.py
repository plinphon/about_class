from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()



while True:
    a = input('What would you like? : ')
    
    if a == 'report':
        coffeemaker.report()
        money.report()
    elif a== 'off':
        quit()
    
    elif menu.find_drink(a) != None:
        drink = menu.find_drink(a)
        if coffeemaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
                coffeemaker.report()
                money.report()





