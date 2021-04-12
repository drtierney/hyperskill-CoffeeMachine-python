WATER = 200
MILK = 50
BEANS = 15

cups = int(input("Write how many cups of coffee you will need:\n"))

print(f'for {cups} cups you will need:')
print(f'{cups * WATER} ml of water')
print(f'{cups * MILK} ml of milk')
print(f'{cups * BEANS} g of coffee beans')
