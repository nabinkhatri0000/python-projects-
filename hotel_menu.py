name =input("Please enter your name beore ordering :")
#menu of the resto 
menu = { "Veg momo":110, 
        "Buff momo": 130,
        "Chicken momo": 150,
        "Black tea": 30,
        "Milk tea": 40,
        "Veg noodels": 100,
        "Egg noodels": 120,
        "Buff noodels": 120,
        "Chicken noodels": 140,
        "Mix noodels": 200,
}

#Greetings 
print(f"Welcome Mr.{name} in our resto please select your order  ")
print("Veg momo: 110\nBuff momo: 130\nChicken momo: 150\nBlack tea: 30\nMilk tea: 40\nVeg noodels: 100\nEgg noodels0: 120\nBuff noodels: 120\nChicken noodels: 140\nMix noodels: 200")

total_oreder = 0

item_1 = input("please enter your item to order :")

if item_1 in menu:
    total_oreder += menu[item_1]
    print(f"Your order {item_1} has been added.")
else:
    print(f"The item {item_1} you ordered is not available yet! ")

another_order = input("Would you like to order any thing more ? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter your next order:")
    if item_2 in menu:
        total_oreder += menu[item_2]
        print(f"Your order {item_2} has also been added to your order.")
    else:
        print(f"The item {item_2} is not available yet!")
    print(f"The total bill of your order is Rs. {total_oreder}. Thank you!")

