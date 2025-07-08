from random import randint
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")

number = randint(1, 101)
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {number}")

dif = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0
if dif == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

guess = ""

while guess != number:

    guess = int(input("Make a guess: "))

    if guess < number:
        print("Too low.")
        print("Try again.")
    elif guess > number:
        print("Too high.")
        print("Try again.")

    attempts -= 1

    if attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        break
    elif attempts != 0 and number != guess:
        print(f"You have {attempts} attempts remaining to guess the number.")

if number == guess:
    print(f"You got it! The answer was {number}.")