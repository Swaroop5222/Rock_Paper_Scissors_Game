l1=('rock','paper','scissors')
import random

while(True):
    ask=input("Do you want to play the game?(y/n): ").lower()
    computer=random.choice(l1)
    if ask=='y':
        user=input("Enter rock or paper or scissors: ").lower()
        if user==l1[0] or user==l1[1] or user==l1[2]:
                if (user=='rock' and computer=='scissors') or (user=='paper' and computer=='rock') or (user=='scissors' and computer=='paper'):
                 print('Computer choice: ',computer)
                 print("You Won")
                elif (computer=='rock' and user=='scissors') or (computer=='paper' and user=='rock') or (computer=='scissors' and user=='paper'):
                 print('Computer choice: ',computer)
                 print("Computer Won") 
                else:
                 print('Computer choice: ',computer)
                 print("Draw")
        else:
          print("Enter either \'rock\' or \'paper\' or \'scissors\' only")
    elif ask=='n':
       print("Game completed")
       break
    else:
       print("Enter either \'y\' or \'n\'")
      