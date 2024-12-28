print("Welcome to my computer quiz!")

playing = input("Do you want to play: ")

if playing.lower() != "yes":
    quit()   

print("Okey! Let's play :) ")
score = 0

answer = input("What is part Memory that stores temporary data? ")  
if answer.lower() == "ram":
    print('Correct!') 
    score += 1
    
else:
    print("Incorrect!")

answer = input("The physical parts of a computer.what is that? ")  
if answer.lower() == "hardware":
    print('Correct!')
    score += 1 
    
else:
    print("Incorrect!")
    
answer = input("What is he brain of the computer? ")  
if answer.lower() == "cpu":
    print('Correct!') 
    score += 1
    
else:
    print("Incorrect!")   
    
answer = input("A copy of data for safety.What is it call? ")  
if answer.lower() == "backup":
    print('Correct!')
    score += 1 
    
else:
    print("Incorrect!") 

answer = input("What call the name of Harmful software that can damage a computer. ")  
if answer.lower() == "virus":
    print('Correct!')
    score += 1 
    
else:
    print("Incorrect!")     

print("You Got " + str(score) + "questions correct! ")         