import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while yes_no == "y":
    print(art.logo)

    your = []
    computer = []
    total_your = 0
    total_computer = 0

    # First card of player
    card_your = random.choice(cards)
    total_your += card_your
    your.append(card_your)

    # Second card of player
    card_your = random.choice(cards)
    total_your += card_your
    your.append(card_your)

    # First card of computer
    card_computers = random.choice(cards)
    total_computer += card_computers
    computer.append(card_computers)

    print(f"Your cards: {your}, current score: {total_your}")
    print(f"Computers first card: {computer[0]}")

    if total_your == 21:
        print("BlackJack! You win.")
        yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        continue

    cont = input("Type 'y' to get another card, type 'n' to pass: ")

    while cont == 'y':
        # Third or more card of player
        card_your = random.choice(cards)
        total_your += card_your
        your.append(card_your)

        if 11 in your and total_your > 21:
            your[your.index(11)] = 1
            total_your = sum(your)


        print(f"Your cards: {your}, current score: {total_your}")
        print(f"Computers first card: {computer[0]}")

        if total_your > 21:
            print(f"Your cards: {your}, final score: {total_your}")
            print(f"Computers first card: {computer[0]}")
            print("You lose :(")
            break
        elif total_your == 21:
            print(f"Your cards: {your}, final score: {total_your}")
            print(f"Computers first card: {computer[0]}")
            print("BlackJack! You win.")
            break
        else:
            cont = input("Type 'y' to get another card, type 'n' to pass: ")

    if cont == 'n' and total_your <= 21:
        while total_computer < 17:
            # Second or more card of computer
            card_computers = random.choice(cards)
            total_computer += card_computers
            computer.append(card_computers)

            if 11 in computer and total_computer > 21:
                computer[computer.index(11)] = 1

        print(f"Your cards: {your}, final score: {total_your}")
        print(f"Computer's cards: {computer}, final_score: {total_computer} ")

        if total_your < total_computer:
            print("You lose :(")
        elif total_your == total_computer:
            print("Draw.")
        else:
            print("You win :)")

    yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")