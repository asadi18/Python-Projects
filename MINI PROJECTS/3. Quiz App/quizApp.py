questions = [
{
    "promp": "What is the Capital of Bangladesh ? ",
    "options":["A. Sylhet", "B.CTG", "C. Dhaka"],
    "answer": "C"
    
},
{
    "promp": "What is the National Fish of Bangladesh ?",
    "options": ["A. Elsha", "B. Rupchada", "C.Pankgash"],
    "answer": "A"
    
},
{
    "promp": "When Bangladesh Formed ? ",
    "options": ["A. 1952", "B. 1980", "C. 1971"],
    "answer": "C"
    
},
{
    "promp":"Who is the neighber Country of Bangladesh ?",
    "options":["A. USA", "B. India", "C.UK"],
    "answer": "B"}    
]

def quizApp(x):
    score = 0
    for question in x:
        print(question["promp"])
        for option in question["options"]: 
            print(option)
        userIn = input("Enter The answer here A,B OR C : ").upper()
      
        if(userIn == question["answer"]):
            print("Correct Answer !\n")
            score+=1
        else: 
            print("Wrong Answer !\n") 
      
         

    print(f"Your Score is : {score} Out of {len(x)}\n" )     
        
quizApp(questions)