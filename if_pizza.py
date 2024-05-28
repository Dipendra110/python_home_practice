size=input("Which piza do you wanna order(S/M/L)?")
bill=0
if size=='s' or size=='S':
    bill+=100
    print("Small pizza price is Rs.100")
elif size=='M' or size=='m':
    bill+=200
    print("Medium pizza price is Rs.200")
else:
    bill+=300
    print("Medium pizza price is Rs.300")
add_pepperoni=input("Do you want to add pepperoni?(Y/N)")
if add_pepperoni=='y' or add_pepperoni=='Y':
    if size=='s' or size=='y':
        bill+=30
    else:
        bill+=50
add_cheese=input("Do you want to add cheese(Y/N)?")
if add_cheese=='y' or add_cheese=='Y':
    bill+=20
print(f"Your total bill is Rs.{bill}")

