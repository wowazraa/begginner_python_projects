
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${total_money}")

    elif choice == "off":
        is_on = False
        break

    elif choice in MENU:
        if resources["water"] < MENU[choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif ("milk" in MENU[choice]["ingredients"]) and resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins. ")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickles?: "))
            penny = int(input("How many pennies?: "))

            money = quarter / 4 + dime / 10 + nickel / 20 + penny / 100
            
            if money >= MENU[choice]["cost"]:
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                if "milk" in MENU[choice]["ingredients"]:
                    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                total_money += MENU[choice]["cost"]
                return_money = money - MENU[choice]["cost"]
                print(f"Here is ${return_money} in change.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Invalid input. Please choose espresso, latte or cappuccino.")
