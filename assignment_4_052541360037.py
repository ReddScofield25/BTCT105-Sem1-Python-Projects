import random

while True:
    number = random.randint(1, 100)
    guesses = 0
    print("I'm thinking of a number between 1 and 100.")

    while guesses == guesses:
        guess = int(input("Enter your guess: "))
        guesses += 1

        if guess > number:
            print("Too high, try again.")
        elif guess < number:
            print("Too low, try again.")
        else:
            print(f"Congratulations! You guessed it in {guesses} tries.")
            guesses = 0
            number = random.randint(1, 100)
            print("\nI'm thinking of a number between 1 and 100.")