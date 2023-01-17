import random


number = random.randint(1, 100)


guess = int(input("Guess the number: "))


tries = 1


while guess != number:
    if guess > number:
        print("Too high!")
    else:
        print("Too low!")
    guess = int(input("Guess the number: "))
    tries += 1


print("You guessed the number in", tries, "tries!")

