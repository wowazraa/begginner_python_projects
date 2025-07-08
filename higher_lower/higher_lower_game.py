import random
from art import logo, vs
from game_data import data

print(logo)

score = 0
cont = True

num1 = random.randint(0, len(data) - 1)
compA = data[num1]

num2 = random.randint(0, len(data) - 1)
compB = data[num2]

while num2 == num1:
    num2 = random.randint(0, len(data) - 1)
    compB = data[num2]

while cont:

    print(f"Compare A: {compA['name']}, a {compA['description']}, from {compA['country']}")
    followerA = compA['follower_count']
    # print(followerA)

    print(vs)

    print(f"Compare B: {compB['name']}, a {compB['description']}, from {compB['country']}")
    followerB = compB['follower_count']
    # print(followerB)

    choice = input("Who has more followers? Type 'A' or 'B': ")

    if followerB < followerA and choice == "A" or followerB > followerA and choice == "B":
        score += 1
        print(f"You're right! Current score: {score}.")

        if followerB < followerA:
            compA = compA
        else:
            compA = compB

        num2 = random.randint(0, len(data) - 1)
        compB = data[num2]

        while compB == compA:
            num2 = random.randint(0, len(data) - 1)
            compB = data[num2]

    else:
        print(f"Sorry that's wrong. Final score: {score}")
        cont = False