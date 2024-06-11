import random

target = random.randint(1,50)

while True:
    userInput = input("Guess the Number or Type E to exit : ")
    if(userInput == "E"):
        break
    userInput = int(userInput)
    if(userInput == target):
        print("Your Guess is Correct")
        break
    elif(userInput>target):
        print("You have chosen a bigger number, guess smaller than this number")
        
    else:
        print("You have chosen a smaller number, guess a bigger number than this")
        
print("----# Successfully Ended #----")