import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

if choice1 < 0 or choice1 > 2:
    print("Invalid number. Please choose 0, 1, or 2.")
else:
    choice2 = random.randint(0,2)

print(game_images[choice1])
print(f"Computer chose:{game_images[choice2]}")

if choice1 == choice2:
    print("It's a draw.")
else:
    if choice1 == 0:
        if choice2 == 1:
            print("You lose.")
        else:
            print("You win.")
    if choice1 == 1:
        if choice2 == 0:
            print("You win.")
        else:
            print("You lose.")
    if choice1 == 2:
        if choice2 == 1:
            print("You win.")
        else:
            print("You lose.")

