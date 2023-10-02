MENU = {
    'espresso': {
        'ingredients': {
            'coffee': 19,
            'water': 35,
        },
        'price': 1.99,
    },
    'latte': {
        'ingredients': {
            'coffee': 24,
            'water': 50,
            'milk': 150,
        },
        'price': 2.39,
    },
    'flat white': {
        'ingredients':{
            'coffee': 24,
            'water': 60,
            'milk': 50,
        },
        'price': 3.19,
    }
}

INVENTORY = {
    'coffee': 100,
    'water': 300,
    'milk': 300,
    'money': 0,
}

a = input('What would you like? : ')



if a == 'report':
    for i in INVENTORY.items():
        print(f"{i[0]} : {i[1]}")
    quit()

elif a in MENU.keys():
    ingre = MENU[a]['ingredients'].keys()
    for i in ingre:
        if MENU[a]['ingredients'][i] <= INVENTORY[i]:
            continue
        else:
            print(f'Sorry there is not enough {i}.')
            break
else:
    print('Sorry, that is not in menu.')
    quit()

quarters = float(input("insert quarters: ") or 0)
dimes = float(input("insert dimes: ") or 0)
nickels = float(input("insert nickels: ") or 0)
pennies = float(input("insert pennies: ") or 0)

result = 0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennies

price= float(MENU[a]['price'])
if result < price:
    print('Sorry, that\'s not enough money. Money refunded')
    quit()
elif result > price:
    print(f'Here is ${result-price} dollar in change.')

print('Report after purchasing')
for i in INVENTORY.items():
    if not i[0] =='money':
        print(f"{i[0]} : {i[1]- MENU[a]['ingredients'][i[0]] }")
    else:
        change = result - price
        print(f"Money : {change:.2f}")

print(f'Here is your {a}. Enjoy!')