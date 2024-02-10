# # 1.Write program to calculate the area of a rectangle given its length and width.
# length = int(input("Please enter length rectangle: "))  # length of rectangle
# width = int(input("Please enter width of rectangle: "))  # width of rectangle
#
# area = width * length
# print(f"Area of rectangle is: {area} ")  # area of rectangle

# # 2. Create a program that takes a user's name and age as input and prints a greeting message.
#
# name = input("Please enter your name: ")
# age = int(input(f"Hi {name}, please enter your age: "))
#
# if age >= 18:
#     print(f"Congrats {name}, you have chance to change the nation.")
# elif age < 18:
#     remaining_years = 18 - age
#     print(f"sorry! {name}, you have to wait for {remaining_years} more years to vote.")

# #3 Given number is even or odd.
#
# userinput = int(input("Enter a number : "))
#
# if userinput % 2 == 0:
#     print("it is an even number")
# else:
#     print("it is an odd number")

# Given a list of numbers, find a maximum and minimum values
list = []
listlength = int(input("Enter the range of list : "))

for i in range(0,listlength):
    usrinput = int(input(F"Enter the {i} value of list: "))
    list.append(usrinput)
print(f"list = {list}")
print(f"maximum value of list : {max(list)}")
print(f"minimum value of list : {min(list)}")



