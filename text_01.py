print("Welcome to my computer quiz!")

playing = input("Do you want to play: ")

if playing != "yes":
    quit()   

print("Okey! Let's play :) ")

answer = input("What is a computer? ")  
if answer == "A machine that processes and stores information":
    print('Correct!') 
    
else:
    print("Incorrect!")
