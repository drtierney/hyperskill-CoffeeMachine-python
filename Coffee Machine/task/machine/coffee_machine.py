stock_levels = {
    'money': 550,
    'water': 400,
    'milk': 540,
    'coffee beans': 120,
    'disposable cups': 9,
}


def buy():
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu\n')
    if choice == '1':
        if can_make_drink(250, 0, 16):
            stock_levels['water'] -= 250
            stock_levels['coffee beans'] -= 16
            stock_levels['disposable cups'] -= 1
            stock_levels['money'] += 4
    elif choice == '2':
        if can_make_drink(350, 75, 20):
            stock_levels['water'] -= 350
            stock_levels['milk'] -= 75
            stock_levels['coffee beans'] -= 20
            stock_levels['disposable cups'] -= 1
            stock_levels['money'] += 7
    elif choice == '3':
        if can_make_drink(200, 100, 12):
            stock_levels['water'] -= 200
            stock_levels['milk'] -= 100
            stock_levels['coffee beans'] -= 12
            stock_levels['disposable cups'] -= 1
            stock_levels['money'] += 6


def can_make_drink(water_needed, milk_needed, beans_needed):
    if stock_levels.get('water') >= water_needed:
        if stock_levels.get('milk') >= milk_needed:
            if stock_levels.get('coffee beans') >= beans_needed:
                print('I have enough resources, making you a coffee!')
                return True
            else:
                print('Sorry, not enough beans!')
                return False
        else:
            print('Sorry, not enough milk!')
            return False
    else:
        print('Sorry, not enough water!')
        return False


def fill():
    stock_levels['water'] += int(input('Write how many ml of water do you want to add:\n'))
    stock_levels['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    stock_levels['coffee beans'] += int(input('Write how many ml of coffee beans do you want to add:\n'))
    stock_levels['disposable cups'] += int(input('Write how many disposable cups do you want to add:\n'))


def take():
    amount = stock_levels.get('money')
    print(f'I gave you ${amount}')
    stock_levels['money'] = 0


def remaining():
    print()
    print('The coffee machine has:')
    for item in ['water', 'milk', 'coffee beans', 'disposable cups', 'money']:
        print(f'{"$" if item == "money" else ""}{stock_levels.get(item)} of {item}')
    print()


def end():
    exit()


def make_action(action):
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        end()
    else:
        print('Invalid action!')


def main():
    while True:
        act = input('Write action (buy, fill, take, remaining, exit):\n')
        make_action(act)


if __name__ == '__main__':
    main()
