import random
import diagram

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# Rock(0) defeats Scissors(2).
# Scissors(2) defeat Paper(1).
# Paper(1) defeats Rock(0).


ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

comp_ch = random.randint(0,2)
if ch == comp_ch:
    if ch == 0:
        print(diagram.rock + "\n" + diagram.rock)
    elif ch == 1:
        print(diagram.paper + "\n" + diagram.paper)
    elif ch == 2:
        print(diagram.scissors + "\n" + diagram.scissors)
    print("Its a draw!")
else:
    if ch == 0:
        print(diagram.rock)
        if comp_ch == 2:
            print(diagram.scissors)
            print("You Won!")
        if comp_ch == 1:
            print(diagram.paper)
            print("You Lose!")
    elif ch == 1:
        print(diagram.paper)
        if comp_ch == 2:
            print(diagram.scissors)
            print("You Lose!")
        if comp_ch == 0:
            print(diagram.rock)
            print("You Won!")
    elif ch == 2:
        print(diagram.scissors)
        if comp_ch == 0:
            print(diagram.rock)
            print("You Lose!")
        if comp_ch == 1:
            print(diagram.paper)
            print("You Win!")
if ch != 0 and ch != 1 and ch != 2:
    print("Wrong input!")
