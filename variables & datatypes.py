# print("Manas")

# name = "Gautam"
# age = 43
# price = 33.49

# print(name, age, price)

# print(type(name))
# print(type(age)) 
# print(type(price))

# name = 'mg'
# name1 = "mgg"
# name2 = '''mggg'''

# we can use with single, double as well as triple quotes to print.

# print(name, name1, name2)

# age = 23
# old = False
# a = None

# print(type(old))
# print(type(a)) # to know the type of the data


# ===========================================


#arithmetic operators

# a = 9
# b = 4 

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)  # always give in decimal e.g. 2.0
# print(a%b)  # give remainder
# print(a**b) # a to the power b calculate krre h


# ============================================


# relational operators
# always give True & False values

# a = 30
# b = 20

# print(a==b) #False
# print(a!=b) #True
# print(a>b) #True
# print(a<b) #False
# print(a<=b) #False
# print(a>=b) #True


# ============================================


# Assignment Operators

# num = 30

# num +=10
# num-=10
# num*=10
# num/=10
# num**=10

# print("num : ", num)


# =============================================


# Logical Operators  #not
# and -- dono value true hogi to he mai true hoonga
# or -- dono value me se koi v ek value true hogi to mai v true ho jaunga
# works on Boolean values

# a= 50
# b=30
# print(not (a<b))
# print(not False)

# val1 = True
# val2 = False

# print("AND operator:", val1 and val2)
# print("OR operator:", val1 or val2)
# print("OR operator:", (a==b) or (a>b))


# =============================================


# Type COnversion
# conversion - automatic hota h in Python
# catsing - mannual krna hota h

# a = 4
# b = 4.45
# sum = a+b #8.45 --> here type conversion is done by python which is Implict conversion
# print(sum) 
# print(type(sum))

# a = "3"
# b = 32
# c = int(a) + b  # here we did manually conversion string to int, called Type Casting
# print(c)


# =======================================


# Taking input from users


# input("Enter Your Name : ")
# name = input("Enter Your Name : ")
# print("Welcome ",name)

# it always give string value

# age = input("Enter Your Age: ")
# print(type(age), age)

# so, if we want to excat input value with their apropriate data types 
# then we use type casting with input().

# val = int(input("Enter a value: "))
# print(type(val), val) #  ow it's show int data type.

# name = input("Enter Name:")
# age = int(input("Enter Age: "))
# marks = float(input("Enter Marks: "))

# print("Welcome", name)
# print("Age =", age)
# print("Marks =", marks)


# ========================================


# Let's Practice the questions.

# 1. Write a program to input 2 numbers & print their sum.

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# print("Sum of your two numbers is: ",a+b)


# 2. WAP to input side of a square & print it's area.

# side = float(input("Enter the side of a square: "))
# print("Area of the square is:", side * side)
# print("Area of the square is:", side ** 2) # also write like this as well.



# 3. WAP to input 2 floating point numbers & print their average.

# a = float(input("Enter a float number: "))
# b = float(input("Enter a float number: "))

# print("Your average floating number is: ",(a+b)/2)


# 4. WAP to input 2 int numbers, a and b.

# Print True if a is greater than or equal to b. 
# If not print False.

# a = int(input("Enter a integer number: "))
# b = int(input("Enter a integer number: "))
# print(a>=b)
