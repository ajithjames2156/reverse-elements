import random

us = 0
cs = 0

while True:
    l = ["stone", "paper", "scissor"]
    system_choice = random.choice(l)

    print(f'Choose one: ["stone", "paper", "scissor"]')
    user_choice = input("Enter your choice: ")
    print('Computer choice is:', system_choice)

    if user_choice == system_choice:
        print("It's a draw")
        print("User =", us)
        print("System =", cs)

    elif user_choice == "stone" and system_choice == "scissor":
        print("You win!")
        us += 1
        print("User =", us)
        print("System =", cs)
        x = int(input("1 = play again \n2=exit"))
        if x == 2:
            break

    elif user_choice == "paper" and system_choice == "stone":
        print("You win")
        us += 1
        print("User =", us)
        print("System =", cs)
        x = int(input("1 = play again \n2=exit"))
        if x == 2:
            break

    elif user_choice == "scissor" and system_choice == "paper":
        print("You win")
        us += 1
        print("User =", us)
        print("System =", cs)
        x = int(input("1 = play again \n2=exit"))
        if x == 2:
            break

    else:
        print("system win")
        cs+=1
        print("User =", us)
        print("System =", cs)
        x = int(input("1 = play again \n2=exit"))
        if x == 2:
            break




