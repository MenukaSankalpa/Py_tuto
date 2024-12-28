print("Welcome to my computer quiz!")

playing = input("Do you want to play: ")

if playing != "yes":
    quit()   

print("Okey! Let's play :) ")

answer = input("What is part Memory that stores temporary data? ")  
if answer == "ram":
    print('Correct!') 
    
else:
    print("Incorrect!")

answer = input("The physical parts of a computer.what is that? ")  
if answer == "hardware":
    print('Correct!') 
    
else:
    print("Incorrect!")
    
answer = input("What is he brain of the computer? ")  
if answer == "cpu":
    print('Correct!') 
    
else:
    print("Incorrect!")   
    
answer = input("A copy of data for safety.What is it call? ")  
if answer == "backup":
    print('Correct!') 
    
else:
    print("Incorrect!") 

answer = input("What call the name of Harmful software that can damage a computer. ")  
if answer == "virus":
    print('Correct!') 
    
else:
    print("Incorrect!")     
         