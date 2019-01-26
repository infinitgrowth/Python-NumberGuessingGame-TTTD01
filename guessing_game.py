"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import os
clear = lambda: os.system('cls')

    
# Compares the guess to the answer to give the user 
# a prompt to guess higher or lower
def guess_hi_lo(guess, answer):
        if guess > answer:
            return print("It is lower")
        elif guess < answer:
            return print("It is higher")
# Checks the guess for any errors letters or numbers out of range
def guess_try():
    while True:
        try:
            guess_raw = input("Pick a number between 1 and 10:  ")
            int(guess_raw)
        except ValueError:
            print("That guess does not count. Please enter a number between 1 and 10:  ")
            print("(Value entered is not a number)")
        else:
            try:
                guess = int(guess_raw)
                if guess > 10 or guess < 1:
                    raise ValueError("The number entered is out of range")
                

            except ValueError as err:
                print("That guess does not count. Please enter a number between 1 and 10")
                print("({})".format(err))

            else:
                return guess
                #break    

# This is the games main code function
def start_game(scores):
    #print("Hello")
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # Prints the title
    print("-"*36)
    print("Welcome to the number guessing game!")
    print("-"*36)

    #Initiates variables and prompts the user
    guess = 0
    answer = random.randint(1,10)
    guess = guess_try()
    num_of_guesses = 1

    #checks condition that guess is not equal to the answer and keep 
    # asking the user to retry until they succeed
    while answer != guess:

        guess_hi_lo(guess, answer)
        guess = guess_try()
        num_of_guesses += 1

    # Let the user know they succeed
    if num_of_guesses == 1:
        print("You got it. It took you {} try".format(num_of_guesses))
    elif num_of_guesses > 1:
        print("You got it. It took you {} tries".format(num_of_guesses))
    
    #adding to the scores list
    scores.append(num_of_guesses)

    # ask the user if they want to play again 
    # and give them more information on the highscore
    
    play_again = input("Would you like to play the game again? Enter [y]es or [n]o:  ")
    
    # check the list to assign the lowest score as the high score
    high_score = min(scores)
    
    # call the function again
    if play_again.lower() == "y" or play_again.lower() =="yes":
        clear()
        print("-"*36)
        print("High score is {} tries to guess the answer!".format(high_score))
        print("-"*36)
        start_game(scores)
    
    # end the game
    elif play_again.lower() == "n" or play_again.lower() =="no":
        print("-"*36)
        print("Final high score is {} tries to guess the answer! Great job!".format(high_score))
        print("-"*36)
        print("Thank you for playing, please come again soon!")
        print("-"*36)
    
  

if __name__ == '__main__':
    
    #create an empty list to hold the different user scores
    scores = []
    
    # Kick off the program by calling the start_game function.
    start_game(scores)
    
