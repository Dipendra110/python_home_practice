import random
heights=input("Enter the list of height separated by space:")
list_of_height=heights.split(" ")
count=0
for height in list_of_height:
    count=count+1
print(count)
for i in range(count):
    list_of_height[i]=int(list_of_height[i])
print(list_of_height)
sum=0
for j in list_of_height:
    sum=sum+j
print(sum)
print(f"Average height is :{sum/count}")