import random
secret_number = random.randint(1, 100)
guess_count = 0
while True:
    user_guess = int(input("Guess the secret number (between 1 and 100): "))
    
    guess_count += 1
    
    if user_guess == secret_number:
                print(f"Congratulations! You guessed the secret number {secret_number} in {guess_count} guesses.")
                break
    elif user_guess < secret_number:
                print("Too low! Try again.")
else:
    print("Too high! Try again.")