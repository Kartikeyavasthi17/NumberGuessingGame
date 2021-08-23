import random
numberselector =random.randint(1,9)
chances =0
print("Number guessing game")
print("Guess a number (between 1 and 9)")

while chances<5:
    guess=int(input("Enter your guess :" ))

    if guess == numberselector:
        print("Congratulation YOU WON!!!")
        break

    elif not guess == numberselector:
        print("That's wrong try again")    
    
    chances=chances+1     

if  not chances < 5:      
    print("YOU LOSE!!! The number is",numberselector) 