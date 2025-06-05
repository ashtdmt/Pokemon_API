#rock paper scissor game
import random

a=0

while True:

    choices = ["rock","paper","scissor"]
    player = None

    while player not in choices:
        player = input("pick rock, paper or scissor ").lower()

    comp =  random.choice(choices)

    if player==comp:
        print("player: "+player)
        print("computer: "+comp)
        print("It is a tie")
        print("winning streak = "+str(a))
    elif player == "rock":
        if comp == "paper":
            print("player: "+player)
            print("computer: "+comp)
            print("You lose")
            a=0
            print("winning streak = "+str(a))
        if comp == "scissor":
            print("player: "+player)
            print("computer: "+comp)
            print("You win")
            a+=1
            print("winning streak = "+str(a))
    elif player == "paper":
        if comp == "scissor":
            print("player: "+player)
            print("computer: "+comp)
            print("You lose")
            a=0
            print("winning streak = "+str(a))
        if comp == "rock":
            print("player: "+player)
            print("computer: "+comp)
            print("You win")
            a+=1
            print("winning streak = "+str(a))
    elif player == "scissor":
        if comp == "rock":
            print("player: "+player)
            print("computer: "+comp)
            print("You lose")
            a=0
            print("winning streak = "+str(a))
        if comp == "paper":
            print("player: "+player)
            print("computer: "+comp)
            print("You win")
            a+=1
            print("winning streak = "+str(a))

    pa = input("you want to play again(yes/no) ").lower()

    if pa!="yes":
        break
