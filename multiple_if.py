
height=int(input("Whats your height:"))
price=0
if height>=3:
    print("You can ride")
    age=int(input("Enter your age:"))
    if age<=12:
        price=150
        print("Ticket price is 150")
    elif age<=18:
        price=300
        print("Ticket price is 300")
    else:
        price=400
        print("Ticket price is 400")
    want_photo=input("Do you want to take photo(Y/N)?")
    if want_photo=='Y' or want_photo=='y':
        price=price+50
    print(f"Your total bill is {price}.")

else:
    print("You cannot ride")
