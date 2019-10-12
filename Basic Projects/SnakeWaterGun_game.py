import random
from itertools import combinations

chances = 0
human_point = 1
computer_point = 1

players = ['snake', 'water', 'gun']

while chances < 10:
    human_input = input("Type Snake, Water or Gun :\n")
    if (human_input.lower() in players):
        comp_select = random.choice(players)
        if (human_input.lower() == 'water' and comp_select == 'snake'):
            chances += 1
            print("Computer wins you have ", 10 - chances, " chances")
            print(comp_select)
            computer_point += 1
        elif (human_input.lower() == 'gun' and comp_select == 'water'):
            chances += 1
            print("Computer wins you have ", 10 - chances, " chances")
            print(comp_select)
            computer_point += 1
        elif human_input.lower() == 'snake' and comp_select == 'gun':
            chances += 1
            print("Computer wins you have ", 10 - chances, " chances")
            print(comp_select)
            computer_point += 1
        elif human_input.lower() == comp_select:
            print(comp_select)
            chances += 1
            print("Choices draw!!")
            computer_point += 1
            human_point += 1
        else:
            print("You have won!!!")
            chances += 1
            human_point += 1
    else:
        print("Wrong Selection, Please try again!!!")

if human_point > computer_point:
    print("You have won the game!!")
elif human_point < computer_point:
    print("Computer have won the game!")
else:
    print("Match has draw")
