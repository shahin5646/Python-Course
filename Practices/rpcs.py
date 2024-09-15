import random
import sys
from enum import Enum

class game(Enum):
    ROCK = 1
    PAPER= 2
    SCISSORS=3
    
# print(game(2))
# print(game.PAPER.value)
# print(game['SCISSORS'])
#sys.exit()

player_choice =input("Enter a Numbeer:\n 1 for Rock\n 2 for Paper \n 3 for Scissors\n")
player =int(player_choice)
computer_choice =random.choice("123")
computer = int(computer_choice)

if player<1 or player>3:
    sys.exit("You must chose 1,2 or 3 ")

  
print("You choose: " +str(game(player)).replace('game.',' ') )
print("Python choose: "+str(game(computer)).replace('game.',' '))


if player == 1 and computer == 3:
    print("🎉🎉🎉You win !!!!!🎉🎉🎉")
elif player == 2 and computer == 1:
    print("You win !!!!!")
elif player == 3 and computer == 2:
    print("🎉🎉🎉You win !!!!!🎉🎉🎉")
elif player == computer:
    print("😶😐😁  Match Tie  !!!!!")
else:
    print("🎉🎉🎉Python Win !!!!🎉🎉🎉")
    
