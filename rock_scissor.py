import random
def compch():
    choices=['rock','paper','scissors']
    c=random.choice(choices)
    print("Computer Choice :",c)
    return c

def winner(user_ch,computer_choice):
    if user_ch==computer_choice:
        print("Its a TIE!")

    elif user_ch=='rock':
        if computer_choice=='paper':
            print("Computer wins !")
        else:
            print("You win !")
    elif user_ch=='paper':
        if computer_choice=='scissors':
            print("Computer wins !")
        else:
            print("You win !")
    elif user_ch=='scissors':
        if computer_choice=='rock':
            print("Computer wins !")
        else:
            print("You win !")

def game_menu():
    print()
    print("#########Rock,Paper,Scissor Game ############")
    print()
    user_ch=input("Enter rock , paper or scissors: ")
    computer_choice=compch()
    winner(user_ch,computer_choice)

ans='y'
while ans!='q':
    game_menu()
    ans=input("Wanna play again ? Enter to play, type 'q' to quit:").lower()
    


