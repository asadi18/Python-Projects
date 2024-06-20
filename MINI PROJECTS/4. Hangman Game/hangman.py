import random 
words = ['python', 'java', 'kotlin', 'ruby', 'javascript','swift']

#print(random.choice(words)) #To check what is happening

chosenWord = random.choice(words)
wordDisplay = ['_' for _ in chosenWord]
attempt = 8 

print('Welcome to hangman game ! Guess a Programming language by letter each ')

while attempt > 0 and '_' in wordDisplay:
    print("\n" + ' '.join(wordDisplay))
    guess = input("Enter the letter one by one to guess the word:  ").lower()
    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            if letter == guess:
                wordDisplay[index] = guess
                
    else: 
        print("Letter Not Matched, Try Again !!! ")
        attempt -=1
        
if '_' not in wordDisplay: 
    print("You guseed the Word!")
    print(' '.join(wordDisplay))
    print("You Have Won!")
    
else: 
    print("You ran out of attempts. The word was: "+ chosenWord)
    print("You Lost The Game!")