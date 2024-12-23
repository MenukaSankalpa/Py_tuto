print("Welocome to my computer quiz!")
playing=input("Do you want to play it? ")
score=0


if playing.lower()  == "yes":
    print("Ok!")
else :
    print("Ok, Bye!")
    
answer=input('What is the main color in sea? ').lower()
if answer == 'blue':
    print("Correct!")
    score+=1
else:
    print("Wrong!")
    score=score-1

answer=input('What is main thing for crush ice? ').lower()
if answer == 'fire':
    print("Correct!")
    score+=1
else:
    print("Wrong!") 
    score=score-1       
  
answer=input('Who is the precident now? ').lower()
if answer == 'anura':
    print("Correct!")
    score+=1
else:
    print("Wrong!")
    score=score-1    
    
answer=input('How your ex look now?  ').lower()
if answer == 'hot':
    print("Correct!")
    score+=1
else:
    print("Wrong!")
    score=score-1

answer=input('Do know mia kalifa? ').lower()
if answer == 'yes':
    print("You are the Man!")
    score+=1
else:
    print("Like Girl!") 
    score=score-1
    
answer=input('Is AI good or bad?   ').lower()
if answer == 'yes':
    print("Correct!")
    score+=1
else:
    print("Wrong!")
    score=score-1    
 
print("You win " + str(score) + " questions!")
print("You win " + str((score/5)*100) + " % ")    
               