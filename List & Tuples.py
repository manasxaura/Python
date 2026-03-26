# marks = [67.9, 65.7, 78.4, 86.3, 59.1]

# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1])

# # we can add multiple type of data store in a list.

# student = ["Manas", 88.3, 24, "Bangalore"]
# print(student[0])

# # here we can manipulate the data in List. becoz of "List is mutable"

# student[0] = "Binod"
# print(student)


# # also slicing can apply on List.

# print(marks[1:4])

#==========================

# LIST METHODS

# list = [1, 7, 9, 4]

# list.append(2)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# # Also apply on string or character.

# lists = ["Apple", "Guava", "Litchi"]
# lists.sort(reverse= True)
# print(lists)

# list.reverse()
# print(list)

# list1 = [3, 8, 1, 5, 9]

# list1.insert(1, 9)
# print(list1)

# list1.remove(9)
# print(list1)

# list1.pop(2)
# print(list1)

#=-===============-=-=-=-=-=-=-=-=-=-=

# TUPLES

# tup = (1, 7, 5,)
# print(type(tup))
# print(tup[2])

# here we can't manipulate the tupple for example

# tup[1] = 2

#  for only one input in tuple we need to write like this

# tupp = (1,)
# print(tupp)
# print(type(tupp))

# if you write without , comma then it's treat as a integer.

# tuppp = (1)
# print(tuppp)
# print(type(tuppp))


# TUPLES METHODS


# tup = (1, 6, 3, 9, 6)

# # to give the index of that elemnet.
# print(tup.index(3)) 

# # to give the count of that element. 
# print(tup.count(6))

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-

# Let's practice some questions.


# 1. WAP to ask the user to enter names of their 3 favorite
# movies & store them in a list.

# print("Enter the 3 favorite movies.")

# m1 = input("Enter 1st movie name: ",) 
# m2 = input("Enter 2nd movie name: ",) 
# m3 = input("Enter 3rd movie name: ",) 

# list = [m1, m2, m3]

# print(list)


# OR [Using append method]
# ========

# movies = []
# mov1 = input("Enter 1st movie: ")
# mov2 = input("Enter 2nd movie: ")
# mov3 = input("Enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# another way ==========

# movies = []
# mov = input("Enter 1st movie: ")
# movies.append(mov)
# mov = input("Enter 2nd movie: ")
# movies.append(mov)
# mov = input("Enter 3rd movie: ")
# movies.append(mov)

# print(movies)

# another way ==========

# movies= []
# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2nd movie: "))
# movies.append(input("Enter 3rd movie: "))

# print(movies)



# 2. WAP to check if a list contains a palindrome of elements
# hint: use copy() method.

# list = [1,2,3,2,1]
# list_copy = list.copy()

# list_copy.reverse()

# if(list_copy == list):
#     print("Palindrome Number")
# else :
#     print("Not Palindrome")


# 3. WAP to count the number of students with the "A" grade in the
# following tuple.

# garde = ["C", "D", "A", "A", "B", "B", "A"]

# print(garde.count("A"))


# 4. Stroe the above values in a list & sort them from "A" to " D".

# list = ["C", "D", "A", "A", "B", "B", "A"]

# list.sort()
# print(list)