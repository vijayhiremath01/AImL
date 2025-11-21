# Number guessing game 
import random 

numberGuess = random.randint(1 , 100)

while True :
    userGuess = int(input("Enter your guess between 1 to 100 : "))
    if userGuess < numberGuess :
        print("Tooo low ! Try again ! ")
    elif userGuess > numberGuess :
        print("Tooo high ! Try again ! ")
    else :
        print("Congrats ! You guessed it right ! ")
        break 
