from random import randint
# moves for the player
moves = ['stone', 'paper', 'scissors']

while True:
    computer = moves[randint(0, 2)]
    player = input("stone, paper, or scissors? (or end the game) ").lower()
    if player == "end the game":
        print("***the game has been ended.***")
        break
    elif player == computer:
        print("tie!")

    elif player == "stone":
        if computer == "paper":
            print("you will lose!!", computer, "beats", player)
        else:
            print("you will win!!", player, "beat", computer)

    elif player == "paper":
        if computer == "scissors":
            print("you will lose!!", computer, "beats", player)
        else:
            print("you will win!!", player, "beats", computer)

    elif player == "scissors":
        if computer == "stone":
            print("you will lose!!", computer, "beats", player)
        else:
            print("you will win!!", player, "beats", computer)
    else:
        print("*****check the spelling******")
