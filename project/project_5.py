import random
randNumber=random.randint(1,100)

userGuess=None
guess=0


while (userGuess != randNumber):
    userGuess= int(input("Enter your Guess number :"))
    guess+=1
    if (userGuess==randNumber):
        print("Your Guess is Right!")

    else:
        if (userGuess>randNumber):
            print("Your Guess is Wrong! please Enter smaller number ! ")
        else:
            print("Your Guess is Wrong! please Enter large number ! ")



print(f"you Guess number is {userGuess} Guesses")

    
    