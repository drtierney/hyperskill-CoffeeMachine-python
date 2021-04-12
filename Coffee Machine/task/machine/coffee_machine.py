water_stock = int(input("Write how many ml of water the coffee machine has:\n"))
milk_stock = int(input("Write how many ml of milk the coffee machine has:\n"))
beans_stock = int(input("Write how many grams of coffee beans the coffee machine has:\n"))

required_cups = int(input("Write how many cups of coffee you will need:\n"))

cups_per_water = water_stock // 200
cups_per_milk = milk_stock // 50
cups_per_beans = beans_stock // 15

max_cups = min(cups_per_water, cups_per_milk, cups_per_beans)

if required_cups < max_cups:
    print(f"Yes, I can make that amount of coffee (and even {max_cups - required_cups} more than that)")
elif required_cups > max_cups:
    print(f"No, I can make only {max_cups} cups of coffee")
else:
    print("Yes, I can make that amount of coffee")
