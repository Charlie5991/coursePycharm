import random


def main():
    num = random.randint(0, 100)
    guessed = False
    print("Welcome to the HI - LO game")
    while not guessed:
        guess_num = int(input("Guess a number between 1 & 100: "))
        if num == guess_num:
            guessed = True
        if num > guess_num:
            print("Too low!")
        if num < guess_num:
            print("Too high!")
    print("Got it: The number is {}".format(num))


if __name__ == '__main__':
    main()