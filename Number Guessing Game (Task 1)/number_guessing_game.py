#NUMBER GUESSING GAME

import random

def details(name):
    print("\n\t\t Welcome " + str(name) + ", let's play Guessing Game!")
    print('''\n RULES of the game:
          1. The user has to guess the number between 1 to 100
          2. Only 10 attempts will be given to the user to guess the number''')
    game()

def playAgain():
    play = input("Enter 'y' to play again  \nEnter 'n' to exit the game  \nYour choice: ")
    if play == 'y':
        game()
    else:
        quit()

def game():
    randNum = random.randint(1, 100)
    UserGuess = None
    attempts = 0
    
    while attempts < 10:
        while UserGuess!= randNum:
            UserGuess = int(input("\n Enter your guess: "))
            attempts += 1
            if UserGuess == randNum:
                print(f'\t\t Congratulations {name}!! You have guessed the correct number!')
                playAgain()

            else:
                if (UserGuess > randNum):
                    print("\nYour guess is too high.")
                    print("Enter a smaller number\n")
                else:
                    print("\nYour guess is too low.")
                    print("Enter a larger number\n")
            if attempts == 10:
                print("\n\t\t You ran out of attempts!!!\n")
                break
            
    playAgain()


name = input("\n\n Enter your name: ")
details(name)
