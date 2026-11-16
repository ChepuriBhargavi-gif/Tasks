
#coding questions

# Write a Python program that calculates and prints the sum of the squares of 
# numbers from 1 to 5 using a 
# for loop.

sum = 0
for i in range(1,6):
    result = i ** 2
    sum += result
    print(f"{i} square {result}")

print(f"sum of squares {sum}")


# Exercise 2:Countdown
# Write a Python program that uses a 
# while loop to print a countdown from 5 to 1

count = 5
while count > 0:
    print(count)
    count -= 1 


# Exercise 3: Multiplication Table with Nested For Loop
# Write a Python program to print the multiplication table for a user-specified 
# number using a nested for loop


table = int(input("Enter Number"))
for i in range(1,11):
    for j in range(1,2):
        print(f"{table} * {i} = {table * i}")


# Exercise 4 
# Write a Python program that uses a "for" loop to find the sum of all even 
# numbers between 0 and 10 (inclusive).


sum = 0
for i in range(11):
    if i %2 == 0:
        print(i)
        sum += i

print(sum)


# Exercise 5
# Calculate the sum of all numbers from 1 to a given number


user_number = int(input("Enter number"))
sum = 0
for i in range(0,user_number + 1):
    sum += i

print(sum)


# Exercise 6
# Display numbers from a list using loop


list = [24,53,21,22,22]
for i in list:
    print(i)

# Exercise 7
# Display numbers from 10 to 1 using for loo


for i in range(-10,11):
    print(i)



# Exercise 8 
# Write a Python program to print the cube of all numbers from 1 to a given 
# number


user_number = int(input("Enter Number"))
for i in range(1,user_number + 1):
    print(i ** 3)


