### Write a program to find out how many days ,weeks, months we have left if we live until 90 years old...

current_age=int(input("Enter your current age:"))
remaining_age=90-current_age
remaining_days=remaining_age*365
remaining_weeks=remaining_age*52
remaining_month=remaining_age*12
print(f"You have {remaining_days} days,{remaining_weeks} weeks,{remaining_month} months left .\nEnjoy your life fully.")