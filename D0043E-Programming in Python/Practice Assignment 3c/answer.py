import random

secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    guess = input("Guess a number between 1 and 20: ")

    if not guess.isdigit():
        print("Out of range! Guess again.\n")
        continue

    guess = int(guess)
    if guess < 1 or guess > 20:
        print("Out of range! Guess again.\n")
        continue

    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        break

if guess == secret_number:
    print(f"Correct! You guessed it in {attempts} attempts.")
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
