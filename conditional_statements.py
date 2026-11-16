#coding Problems


#1.vowel checker:
#write a python program that takes a character as input and checks whether it is a vowel or not.
#use the if-else statement:

char = str(input("Enter Character"))
if char in "aeiou":
    print("vowel")
else:
    print("not a vowel")


#2.Age Group Classification
#Write a program that takes an age as input and classifis the person into one of the following age groups:
#child : 0-12 years
#Teenager : 13-17 years
#Adult:18-64 years
#senior:65 years and older

age = int(input("Enter Your Age"))
if age < 0 or age > 100:
    print("Please Enter Age between 0 and 100")
elif age >= 0 and age <= 12:
    print(f" Your Age is {age} Your Category is Child")
elif age >= 13 and age <= 17:
    print(f"Your Age is {age} Your category is Teenager")
elif age >= 18 and age <= 64:
    print(f"Your Age is {age} Your Category is Adult")
else:
    print(f"Your Age is {age} Your Category is Senior")


#3.Number Classifier

#write a program that takes an integer as input and classifies if as positive,negative,or zero
#use the if-elif-else statement

num = int(input("Enter Number"))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


#4.Leap Year Checker
#Create a program that checks whether a given year is a leap year or not. A leap year is divisible by 4.but
# not by 100 unless it is divivisible by 400

year = int(input("Enter Year"))
if year %400 == 0 or (year % 100 != 0 and year %4 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#5.Calculator:
#Build a simple calculator program that takes numbers and an operator (+,-,*,/) as input and performs the corresponding operation

num_1 = int(input("Enter Number 1"))
num_2 = int(input("Enter Number 2"))
operation = input("Enter Operations")
if(operation == '+'):
    print(num_1 + num_2)
elif(operation == '-'):
    print(num_1 - num_2)
elif(operation == '*'):
    print(num_1 * num_2)
elif(operation == '/'):
    if num_2 != 0:
        print(num_1 / num_2)
    else:
        print("Cannot divide by zero")
elif(operation == '%'):
    print(num_1 % num_2)
else:
    print("Invalid Operator")




#6.short hand if:
#Rewrite the following code using the short hand if statement


x = 8
result = "even" if x %2 == 0 else "odd"
print(result)

x = 8
print(f"{x} is even") if x %2 == 0 else print(f"{x} is odd")




#7.Discount Calculator:
#Create a program that calculates the final price after applying a dicount. The program should take the original price and the dicount percentage as input



product_price = float(input("Enter Product Price"))
discount = float(input("Enter Discount"))
product_discount = (product_price * discount)/100
product_price -= product_discount
print(f"Product Price After Discount is {product_price}")


#8.BMI Calculator
#Write a program that calculates the Body Mass Index(BMI) using the formula BMI = weight(kg) / height(m) * 2.
#The Program should take weight and height as input


height = float(input("Enter Your Height in m"))
weight = float(input("Enter Your Weight in kg"))
body_mass_index = weight/ height ** 2
print(body_mass_index)