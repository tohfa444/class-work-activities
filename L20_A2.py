import random
while True:
    user_action=input("Enter a choice and the choices are\n Rock, Papers, Scissors")
    possible_action=["Rock","Papers","Scissors"]
    computer_action=random.choice(possible_action)
    print("You chose ",user_action,"\n computer chose ",computer_action)
    if user_action==computer_action:
        print(f"Both players selecter {user_action}.It's a tie")
    elif user_action=="Rock":
        if computer_action=="Scissors":
            print("Rock Smashes scissors.\nYou win ")
        else:
            print("Paper covers rock.\nYou lose")

    elif user_action=="Papers":
        if computer_action=="Scissors":
            print("Scissors cut paper.\nYou lose")
        else:
            print("Paper covers rock.\nYou win")

    elif user_action=="Scissors":
        if computer_action=="Papers":
            print("Scissors cut papers.\nYou win ")
        else:
            print("rock smashes scissors.\nYou lose")
    play_again=input("Do u want play again?\nyes/no\n")
    if play_again=="no":
        break
