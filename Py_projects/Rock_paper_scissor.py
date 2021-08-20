import random
choices = ["Rock","Paper","Scissors"]

player = False
cpu_score = 0
player_score = 0

while True:
    computer = random.choice(choices)
    player = input("Rock, Paper or Scissors? :").capitalize()
    print(player)
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "paper":
            print("You lost",computer, "covers", player)
            cpu_score +=1
        else:
            print("You won",player, "smashes", computer)
            player_score +=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost",computer, "cuts", player)
            cpu_score +=1  
        else:
            print("You won",player, "covers", computer)
            player_score +=1    
    elif player == "Scissors":
        if computer == "Rock": 
            print("You lost",computer, "smashes", player)
            cpu_score +=1
        else:
            print("You won",player, "cuts", computer)
            player_score +=1         

    elif player == "End":
        print("Final Scores :")
        print(f"Cpu_score is {cpu_score}")
        print(f"player_score is {player_score}")
        break        

