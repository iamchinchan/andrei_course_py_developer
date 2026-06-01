from random import randint
import sys

fn, s, e = sys.argv
s = int(s)
e = int(e)
print(f"Welcome to Guessing game")
num = randint(s, e)


def take_guess():
    try:
        guess = int(input(f"Enter a nunmber betwewen: {s} and {e}: "))
        return (
            guess
            if s <= guess <= e
            else print(f"PLease enter number within range only")
        )

    except:
        print(f"Please enter a valind number")


guess = None
while guess != num:
    guess = take_guess()

print(f"You have guessed the hum correctly: {num}")
