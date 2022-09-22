# This is a word game

import random  # This is used to randomly choose an item from a list[] or basically a sequence.
import time  # This module is used to import the actual time from your pc to use in the program.

limit = 6
def print_scaffold(guesses, wd):
    if guesses == 0:
        time.sleep(1)  # This is used to halt the execution of the program for a few seconds.
        # It is a fun way to put the user of the game in short suspense.
        print("_________")
        print("|   |    ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|________")

    elif guesses == 1:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|________")

    if guesses == 2:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|   |    ")
        print("|   |    ")
        print("|        ")
        print("|________")

    if guesses == 3:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|  \|    ")
        print("|   |    ")
        print("|        ")
        print("|________")

    if guesses == 4:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|  \|/   ")
        print("|   |    ")
        print("|        ")
        print("|________")

    if guesses == 5:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|  \|/   ")
        print("|   |    ")
        print("|  /     ")
        print("|________")

    if guesses == 6:
        time.sleep(1)
        print("_________")
        print("|   |    ")
        print("|   O    ")
        print("|  \|/   ")
        print("|   |    ")
        print("|  / \   ")
        print("|________")
        print("\n")

        print("The word was %s." % wd)
        print("\n")
        print("\n You LOSE! TRY AGAIN")
        print("\nWould you like to play again? type y = yes, n = no \n")
        # Take input from user
        again = str(input("> "))
        again = again.lower()
        #  Check Condition if the user given input to yes or no
        if again == "y":
            hangMan()
        elif again == "n":
            exit(0)
        else:
            print("Sorry Wrong Entry!,We have to through you out. ")
            time.sleep(2)
        return


#  function to select a word
def selectWord():
    #  open file in which words are kept
    file = open('FREQ')
    #  read file
    words = file.readlines()
    myword = 'a'

    while len(myword) < 4:  # makes sure word is at least 4 letters long
        myword = random.choice(words)
        myword = str(myword).strip('[]')
        myword = str(myword).strip("''")
        myword = str(myword).strip('\n')
        myword = str(myword).strip('\r')
    myword = myword.lower()
    return myword


def hangMan():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("\nWelcome to Hangman game by Bharpur Dahiya\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)  # This is used to halt the execution of the program for a few seconds.
    # It is a fun way to put the user of the game in short suspense.
    print("The game is about to start!\n Lets's play Hangman!")
    time.sleep(3)

    print_scaffold(guesses, word)
    print("\n")
    print("" + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < limit:
        guess = str(input("> "))
        guess = guess.lower()
        a1 = ' '.join(guess_list)

        if len(guess) > 1:
            print("Stop cheating! Enter one letter")

        elif guess == "":
            print("Don't you want to play? Enter one letter at a time.")

        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(a1)
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1

                time.sleep(1)
                print_scaffold(guesses, word)
                print("Wrong guess. " + str(limit - guesses) + " last guess remaining\n")

                if guesses < limit:
                    print("Guess again.")
                    print(' '.join(blanks_list))

            elif word_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WIN! Here is your prize:")
                    print("\n")
                    print("Would you like to play again?")
                    print("Type y for yes or n for no.")
                    again = str(input("> "))
                    if again == "y":
                        hangMan()
                    elif again == "n":
                        break
                    else:
                        print("Sorry you enter wrong entry we should through you out")
                        break

                else:
                    print("Great guess! Guess another!")


hangMan()
