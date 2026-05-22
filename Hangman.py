import random

words = ["apple", "tiger", "house", "green", "water"]

word = random.choice(words)
print("Welcome to Hangman Game")
guessed = []
attempts = 6

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

    if all(letter in guessed for letter in word):
        print("You Won!")
        break

if attempts == 0:
    print("You Lost!")
    print("Word was:", word)