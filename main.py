import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

def guessingGame():
    print("Welcome to my guessing game. You will be asked \nto choose a number and if you guess the correct\none, you win! Good Luck!")
    play = ''
    best_play = sys.maxsize

    while(play != 'no' and play != 'n' and play != 'o'):
        count = 0
        number = random.randint(1,10)
        guess = ''
        while(guess != number):
            guess = int(input("Enter a number 1-100: "))
            count += 1
            if(guess == number):
                print("Congrats, you guessed the number!")
            else:
                print("Not there yet, keep trying.")
    
        print("You guessed in {} tries.".format(count))

        if (count < best_play):
            print('You got a bit luckier this time. New HighScore = {}'.format(count))
            best_play = count

        play = input("Play again? (Yes or No)").strip().lower()

guessingGame()
