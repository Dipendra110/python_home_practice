###Write a program to select a random name from a list of names and the person selected will pay for everybody's food bill
import random
name_list=(input("Enter everybody name separated by comma: "))
split_name=name_list.split(",")
print(split_name)
# choice_name=random.choice(split_name)
# print(f"{choice_name} will pay the bills")
length=len(split_name)
random_choice=random.randint(0,length-1)
print(f"{split_name[random_choice]} will pay the bills")