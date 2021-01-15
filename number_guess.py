# Code modified by Natalie Borgorez

"""This program rolls a pair of dice
and asks the user to guess the sum.
"""

from random import randint
from time import sleep


def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess


def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print('The maximum possible value is: %i' % max_val)
    guess = get_user_guess()
    if guess > max_val:
        print("Your guess is invalid.")
    else:
        print("Rolling...")
        sleep(2)
        print('The 1st roll is: %i' % first_roll)
        sleep(1)
        print('The 2nd roll is: %i' % second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print('The total value is: %i' % total_roll)
        print("Result...")
        if guess == total_roll:
            print("You won!")
            sleep(1)
        else:
            print("You lost. Try again!")


roll_dice(6)

# Code modified by Natalie Borgorez