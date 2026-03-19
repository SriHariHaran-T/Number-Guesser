import random
number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess== number:
    print("Congratulations! You guessed the number.")
elif guess < number:
    print("Too low! Try again, but the number is higher: ", number)
else:
    print("Sorry, the number was:", number)
