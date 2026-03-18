# STRINGS

#=============================

# name = "Manas"
# print(len(name)) # to know the length of string.
# # output: 5


# str1 = "This is a series of Python course."
# print(len(str1)) # 34

#=============================

# str2 = "This is a series of Python course.\nAnd this is 2nd lecture."

# # \n is the escape sequence character, jo ki next line me 
# # print krta h.. remaing part of th string.
# # \n for next line.
# # \t for tab space.
# print(str2)

#=============================

# to join two string, called concatination.

# str1 = "Manas"
# str2 = "Gautam"
# str3 = str1 +" " +str2
# print(str3)
# print(len(str3))

#=============================

#Indexing {start with 0}

# str = "Manas_Gautam"
# print(str[0], str[5])

# str[5] = "@" # not allowed.

# so, in python, we access characters through 
# indexing, but can't manipulate

#=============================

#Slicing: Accessing parts of a string.

# str[starting_index : ending_index] 
# #ending index is not included.

# str = "ManasGautam"
# # str[2:8] is "nasGau" 
# print(str[2:8])

# str[ :4] is same as str[0:4]
# str[1: ] is same as str[1:len(str)]

#negative index
#backward counting

# M a n a s
#-5-4-3-2-1

# str = "Manas"
# print(str[-3:-1]) # "na"

#=====================================

# STring Functions

# str = "i am power."

# str.endswith("er.") #returns True if string ends with substr
# str.capitalize() #capitalizes 1st char. Only works on this time, if i want to again print str then it will not capitilize first character
# str = str.capitalize() # now the original string will affect.
# str.replace(old, new) #replaces all occurences of old.

# print(str.replace("o", "a")) #replace all "o" to "a".
# print(str.replace("power", "strong"))

# str.find(word) #returns 1st index of 1st occurrer.

# print(str.find("am")) # 2

# str.count("word") # counts the occurence of substr

# print(str.count("am")) # 1 : becoz the word "am", appears one time in str.

#=================================

# Let's Paractice few questions of String.


#1. WAP to input user's first name & print it's length.

# str = input("Enter your first name: ")
# print("Your first name length is: ", len(str))


#2. WAP to find the occurrence of '$' in a String.

# str = "hii, $ I am the $ symbol"
# print(str.count("$"))