import random

print(" 0 for Rock\n 1 for Paper \n 2 for Scissors")
user_choice = int(input())
if user_choice > 2 or user_choice < 0:
    print("Please enter valid number")
else:
    comp_choice = [0, 1, 2]
    rand_comp_choice = random.choice(comp_choice)
    print(rand_comp_choice)
    if user_choice == rand_comp_choice:
        print("Draw")
    elif user_choice == 0 and rand_comp_choice == 2:
        print("You win")
    elif user_choice == 2 and rand_comp_choice == 0:
        print("You lose")
    elif user_choice < rand_comp_choice:
        print("You lose")
    elif user_choice > rand_comp_choice:
        print("YOu win")

