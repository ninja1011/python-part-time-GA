# This is HomeWork 1. Multiple problems will be solved here.

# Problem 1: Find Area of Triangle while taking user input
width = float(input("Please enter width of rectangle"))
length = float(input("Please enter length of rectangle"))
area = width * length
# print out the length, width and area
print("The length of the rectangle is", length)
print("The width of the rectangle is", width)
print("The area of the rectangle is", area)


# Problem 2: Convert Celsius to Fahrenheit
# we will take user input for this as well
celsius = float(input("Please enter the degrees in Celsius that you would like converted"))
fahrenheit = (celsius * 9/5) + 32
#print out the degrees in celsius and the converted fahrenheit
print("The degrees in Celsius that you entered,", celsius, ", is", fahrenheit, "degrees Fahrenheit")


# Problem 3: Convert Fahrenheit to Celsius
# we will take user input for this again
fahrenheit = float(input("Please enter the degrees in Fahrenheit that you would like converted"))
celsius = (fahrenheit - 32) * 5/9
#print out the degrees in fahrenheit and the converted celsius
print("The degrees in Celsius that you entered,", fahrenheit, ", is", celsius, "degrees Fahrenheit")


# Problem 4: Take a number from the user and print a message for whether the number is even or not
num = float(input("Please enter a number so we can check if it is odd or even"))
# use an if statement to check if the remainder of the number divided by 2 is zero.
if num % 2 == 0:
    print("The number", num, "is an even number")
else:
    print("The number", num, "is odd")


# This section will print out answers to the second part of the homework
print("A Tuple is group of immutable objects. The difference between a List and a Tuple is the immutability of the objects. Lists are mutable")
print("Variables, also referred to as objects, are place holders in memory for information")
print("The ** operator is used as an exponent.")
name = "john54"
# Capitalizes the first letter in the string
print(name.capitalize())
# Checks is the string is Alphanumeric
print(name.isalnum())
# Converts string into a list
print(name.split())
