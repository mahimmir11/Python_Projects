import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += guess

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
        elif guess < answer:
            print("Too low!,Try Again")
        elif guess > answer:
            print("Too High! Try Again")
        else:
            print(f"CORRECT! The answer is {answer}")
            is_running = False

    else:
        print("Invalid Input")
        print(f"Please select a number between {lowest_num} and {highest_num}")
