import random
secret_number = random.randint(1, 100)

for attempt in range(1, 11):
    user_guess = int(input(f"Guess {attempt}: Guess the secret number (beteween 1 and 100): "))
    if user_guess == secret_number:
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempt} attempts.")
        break
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Sorry, you've used all 10 attempts. The secret number was {secret_number}.")