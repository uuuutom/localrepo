import random

list = ["rock","paper","scissor"]

user_choice = input("Enter your choice (rock, paper, scissor): ")
com_choice = random.choice(list)

if com_choice == user_choice:
    print("It's a tie!")
    
if com_choice == "rock" :
    if user_choice == "paper":
        print(f"Computer choose {com_choice} You win!")
    else:
        print(f"Computer choose {com_choice} Computer wins!")
        
if com_choice == "paper":
    if user_choice == "rock":
        print(f"Computer choose {com_choice} Computer wins!")
    else:
        print(f"Computer choose {com_choice} You win!")
        
if com_choice == "scissor":
    if user_choice == "rock":
        print(f"Computer choose {com_choice} You win!")
    else:
        print(f"Computer choose {com_choice} Computer wins!")
        