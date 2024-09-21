print("Welcome In My Number Guessing Game")
print("Lets Start The Game🎮🎮")
import random
random_number = random.randint(89,99)
tries = 1
username = input("Hello, What's your Name : ")
print("Hello", username+",", )
question = input("Would you Like To Play A Game ? [Y/N] ")
if question == "n" or question == 'N':
    print("oh..okay")
if question == "y" or question == 'Y':
    print("I'm Thinking Of A Number Between 89 & 99")
    guess = int(input("Have a Guess :"))
    if guess > random_number:
        print("Guess Lower...")
    if guess < random_number:
        print("Guess Higher...")
    while guess != random_number:
        tries += 1
        guess = int(input("Try Again : "))
        if guess < random_number:
            print("Guess Higher...")
    if guess == random_number:
        print("You're correct! you win the cash 20000 dollar! The Number Was", random_number, "and it only", tries, "tries!")
