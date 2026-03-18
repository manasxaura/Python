# CONDITIONAL STATEMENTS

# if-elif-else (SYNTAX)

# if(condition):
#     statement1
# elif(condition):
#     statement2
# else:
#     statementN


# light = input("Mention the color of traffic light: ")

# if(light == "red"):
#     print("Stop")
# elif(light == "green"):
#     print("Go")
# elif(light == "yellow"):
#     print("Wait & Look")
# else:
#     print("Invalid Color")


# age = 17

# if(age>=18):
#     print("can vote")
# else:
#     print("cannot vote")


# marks = int(input("Enter your marks: "))

# if(marks >= 90):
#     print("Grade A")
# elif(marks >= 80 and marks < 90):
#     print("Grade B")
# elif(marks >= 70 and marks > 80):
#     print("Garde C")
# else:
#     print("Grade D")


#=============
# nesting

# age = int(input("Enter a age: "))

# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")


#=================================

# Let's practice few questions of Conditional Statements.


#1. WAP to check if a number entered by the user is odd or even.

# num = int(input("Enter a number: "))

# if(num%2 == 0):
#     print("Even")
# else:
#     print("Odd")


#2. WAP to find the greatest of 3 numbers entered by the user.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if(num1 >= num2 and num1 >= num3):
#     print("Greatest Number is: ", num1)
# elif(num2 >= num3):
#     print("Greatest Number is: ", num2)
# else:
#     print("Greatest Numer is: ",num3)


#3. WAP to check if a number is a multiple of 7 or not.

# num = int(input("Enter a number: "))
# if(num%7 == 0):
#     print("Number is divisible by 7")
# else:
#     print("Number is not divisible by 7")
    
