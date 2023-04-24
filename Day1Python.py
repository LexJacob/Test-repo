# This is how you make a comment. 
# This does not show on the webpage

# print ("Beware of Badgers")
# print ("Hello World!")

# key = value 
# AZ = "us-east-1a"

# print(AZ)
# print("us-east-1a")

# + sign adds the next statement or variable
# creates one string
# print(AZ + "and us-east-1b")

# if you are working with numbers it sums the number
# no quotation marks
# num = 7
# print(num + 7)

# Data Types
# Strings
# int -- intiger(?)
# double
# float
# boolean -- true or false

# boolean
# print(AZ == num) # will print as False
# print(AZ == "us-east-1a") # will print as True
# print(" ") # creates a space/next line
# print("10" == 10) # will print False due to different types 

# == equating values
# differing types affect whether two items are the same. not just their values

# Operators 
# == compares values for equivalency
# != compares values for non-equivalency (not equal)
# >; =>; <; <=; 

# CONDITIONS
# + -- adds values
# - -- subtracts values
# * -- multiplies values
# / -- divides values
# % -- modules. gives remainder after dividing two numbers



# CONJUNTIONS
# and -- retuns true if BOTH statements are true
# or -- returns true is atleast ONE of the statments is true
# not -- reverses the value of a boolean expression -- not(10 == 10)
# print(10 == 10 and 10 == "10") # will print out False
# print(10 == 10 or 10 == "10") # will print out True

# CONDITINAL STATEMENTS
# if -- makes decisions

# stateOfBeing = "meh"
# dayOfWeek = "Monday"

# if(stateOfBeing == "tired and worn out" and (dayOfWeek =="Thursday" or "Friday")):
#     print("drink coffee")
# elif(stateOfBeing == "tired"): 
#     print("Must suck to be so tired LOL")
# elif(dayOfWeek == "Monday"):
#     print("Mondays amIright?")
# else: # will print if the statement is false
#     print("have some tea")

# print("Have a nice day!")

# loop 
# for
# while

# numberOfDay = 7

# monthOfYear = 10
# for x in range(0, monthOfYear):
#     print(x)
# print("dine with loop")

# infinite loop
# while numberOfDay < 10:
#     print("looping")

# nameOfDay = "T"

# while nameOfDay != "Tuesday":
#     if (nameOfDay == "Tuesda"):
#         nameOfDay += "y"
#     print("looping")

# print("finished")

# better for executing loops based on conditions
# i = 0
# print(nameOfDay)
# while nameOfDay != "Tuesday":
#     if (nameOfDay == "T"):
#         nameOfDay += "u"
#         print(nameOfDay)
#     elif (nameOfDay == "Tu"):
#         nameOfDay += "e"
#         print(nameOfDay)
#     elif (nameOfDay == "Tue"):
#         nameOfDay += "s"
#         print(nameOfDay)
#     elif (nameOfDay == "Tues"):
#         nameOfDay += "d"
#         print(nameOfDay)
#     elif (nameOfDay == "Tuesd"):
#         nameOfDay += "a"
#         print(nameOfDay)
#     elif (nameOfDay == "Tuesda"):
#         nameOfDay += "y"
#         print(nameOfDay)
#     else:
#         nameOfDay = "Tuesday"
#         print(nameOfDay)
# i = 1

# print (i)

x = 5
if not(x > 0): 
    print("Hello Python")
else:
    print("Hello World")
    
#              0  1  2  3  4  5
myFirstList = [1, 2, 3, 4, 5, 6]

# print(len(myFirstList))

# for i in range(len(myFirstList)):
#     print(i)

# print(myFirstList[1]) # will print 2

# list
myFirstList.append("string")

# for i in myFirstList:
#     print(i)

# for i in range(len(myFirstList)):
#     print(str(i).upper())

print(myFirstList[1:6]) # -- slicing
myFirstList[0] = 0 # will change the first item into 0

# Tuple -- immutable list -- CAN'T be changed
myFirstTuple = (1, 2, 3, 4, 5, 6)
myFirstTuple[0] = 0 # will not change tuple

tupleMyFirstList = tuple(myFirstList) # creates a new tuple list with your myFirstList

