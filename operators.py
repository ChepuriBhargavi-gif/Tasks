#coding exercise

#1. Write a python program to calculate the area of a rectangle using the 
# given formula area = lenght * width. Take the values of length and width 
# as inputs from the user


length = int(input("Enter Length"))
width = int(input("Enter Width"))
result = length * width
print(f"length Value is {length} Width Value is {width} Result is {result}")



#2.Write a python program to demostrate incremeting and decrementing a variable


number = 1000
print(f"Number is {number}")
number += 2000
print(f"Increment By 2000 = Number is  {number}")
number -= 2000
print(f"Decrement By 2000 = Number is {number}")


#3.Write a python program to convert temperature from celsius to fahrenheit.
# The formula for converion is : f = (c * 9/5) + 32. Take the temperature in 
# Celsius as input from the user


celsius = float(input("Enter Celsius Value"))
celsius_to_fahrenheit_F = (celsius * 9/5) + 32
print(f"Celsius value is {celsius} Fahrenheit Value is {celsius_to_fahrenheit_F} F")


#4.Write a Program to calculate the simple interest given the principal amount,rate, 
# and time(in years)

principal_amount = float(input("Enter Principal Amount"))
rate = float(input("Enter Rate"))
time = float(input("Enter Time"))
result = (principal_amount * time * rate)/100
print(f"Principal Amount is {principal_amount}\nRate is {rate}\nTime is {time}\nSimple Interest = {result}")



#5.Write a python program to concatenate two strings and display the result.
# The strings should be taken as input from the user

str_1 = input("Enter Any String")
str_2 = input("Enter Other String")
result = str_1 + str_2
print(result)



#6.Write a python program to convert a distance from kilometers to miles


kilometers = float(input("Enter Kilometers"))
kilometers_to_miles = kilometers * 0.621
print(kilometers_to_miles)




#7.Creat a program that takes user input for their name and age. Use formatted strings 
# to print a message welcoming to user and stating their age


name = input("Enter Your Name")
age = int(input("Enter Your Age"))
print(f"Welcome {name} Age is {age}")


#8.Create a list called numbers that contains integers from 1 to 10

#1. check if the number 5 is in the list
#2. check if the number 15 is not in the list


numbers = [1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)
