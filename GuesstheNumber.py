#program for generating random number 

import random
guess=0
guessCount=0
print("Enter your name")
name=input()
number =random.randint(0,9)
print(name+",I have thought of a number between 0 and 9")
#This is just to debug the program , comment out printing the number once it works
#print (number)

while guessCount <5:
    guessCount= guessCount+1
    print("You have 5 chances .Take a guess please "+ name )                                    
    guess=int(input())
    

    if guess<number:
        print("Guess is low !!")
    if guess> number: 
        print ("Guess is high ")
        
    if guess==number :
        break


if guess==number:
    guessCount=str(guessCount)
    print(" Wow!!, you guessed the correct number in " +guessCount+ " guesses")

if guess!=number:
    number=str(number)
    print("The number I had in my mind was"+number)


print("Press any key to exit" )
value=input()
