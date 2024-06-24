import random

print("Welcome to Rock, Paper and Scissor Game. Enter any one words on input")
user = input("Enter Your Choice: ")
gameValue = ["Rock", "Paper", "Scissor"]

computerChoice = random.choice(gameValue)

if(user == computerChoice):
    print("Computer Choosed", computerChoice, "And", )
    print("Tie")
    
elif(computerChoice == "Rock"):
    if(computerChoice=="Paper"):
        print("Computer Choosed", computerChoice, "And", "Paper Covers the Rock and Computer Wins !!! ")    
    else:
        print("Computer Choosed", computerChoice, "And", "Rock Smashes Scissor and You Win !!! ")
    
elif(computerChoice == "Paper"):
    if(computerChoice=="Scissor"):
        print("Computer Choosed", computerChoice, "And", "Scissor cuts paper and Computer Wins !!! ")    
    else:
        print("Computer Choosed", computerChoice, "And", "Paper covers Rock and You Win !!! ")
        
        
elif(computerChoice == "Scissor"):
    if(computerChoice=="Paper"):
        print("Computer Choosed", computerChoice, "And", "Scissor cuts paper and You Win !!! ")    
    else:
        print("Computer Choosed", computerChoice, "And", "Rock Smashed By Scissor and Computer Win !!! ")
        
else: 
    print("Enter the Correct input with proper Spelling")
    