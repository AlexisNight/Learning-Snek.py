"""Hangman Game: This is a word guessing game where
the player has to guess a word within a certain number
of attempts. You can write a program that randomly
selects a word from a list and allows the user to guess
letters until they have either guessed the word or used
up all of their attempts."""

import time

name = input("What is your name?")

print("Hello, " + name, "Time to play hangman!")

time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

word = ("secret")

guesses = ''

turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=""),
        else:
            print("_", end=""),

            failed += 1
    print("")

    if failed == 0:
        print("You won")
        break
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")

        print("You have", + turns, 'more guesses')

    if turns == 0:
        print("You Lose")