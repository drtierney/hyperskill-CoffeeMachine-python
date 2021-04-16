
stock_levels = {
    'money': 550,
    'water': 400,
    'milk': 540,
    'coffee beans': 120,
    'disposable cups': 9,
    }


def summary():
    print()
    print('The coffee machine has:')
    for item in ['water', 'milk', 'coffee beans', 'disposable cups', 'money']:
        print(f'{stock_levels.get(item)} of {item}')
    print()


def buy():
    choice = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n'))
    if choice == 1:
        stock_levels['water'] -= 250
        stock_levels['coffee beans'] -= 16
        stock_levels['disposable cups'] -= 1
        stock_levels['money'] += 4
    elif choice == 2:
        stock_levels['water'] -= 350
        stock_levels['milk'] -= 75
        stock_levels['coffee beans'] -= 20
        stock_levels['disposable cups'] -= 1
        stock_levels['money'] += 7
    elif choice == 3:
        stock_levels['water'] -= 200
        stock_levels['milk'] -= 100
        stock_levels['coffee beans'] -= 12
        stock_levels['disposable cups'] -= 1
        stock_levels['money'] += 6
    else:
        print('Invalid choice!')


def fill():
    stock_levels['water'] += int(input('Write how many ml of water do you want to add:\n'))
    stock_levels['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
    stock_levels['coffee beans'] += int(input('Write how many ml of coffee beans do you want to add:\n'))
    stock_levels['disposable cups'] += int(input('Write how many disposable cups do you want to add:\n'))


def take():
    amount = stock_levels.get('money')
    print(f'I gave you ${amount}')
    stock_levels['money'] = 0


def make_action(action):
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    else:
        print('Invalid action!')


def main():
    summary()
    while True:
        act = input('Write action (buy, fill, take):\n')
        make_action(act)
        summary()
        break


if __name__ == '__main__':
    main()
