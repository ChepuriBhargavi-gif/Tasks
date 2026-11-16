
# Task 1: Add Function

# Write a Python function named add that takes two arguments a and 
# b and returns their sum 


def add(a,b):
    return a + b
print(add(1,4))



# Task 2: Square Function

# Write a Python function named square that takes a number x as input and returns its square


def square(x):
    return x * x
print(square(4))



# Task 3: Factorial Function

# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.





def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(fact(5))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1)
print(fact(5))



# Task 4: Maximum Function

# Write a Python function named maximum that takes a list of numbers as input and 
# returns the maximum value in the list.


def maximum(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum
print(maximum([1,2,3,4,5,50,40,100,20]))




# Task 5: Reverse Function

# Write a Python function named reverse that takes a string s as input and returns its reverse


def reverse(s):
    reversed = ""
    for i in range(len(s)-1,-1,-1):
        reversed += s[i]
    return reversed
print(reverse("hello"))    



# Task 6: Check Prime Function

# Write a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise 



def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(is_prime(2))



# Task 7: Fibonacci Function

# Write a Python function named fibonacci that takes a positive integer 
# n as input and returns the False .


def fibanacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a,b = b , a + b
fibanacci(10)


# Task 8: Palindrome Function

# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .



def palindome(s):
    reversed = ""
    for i in range(len(s)-1,-1,-1):
        reversed += s[i]
    if reversed == s:
        return "Palindrome"
    return "Not a Palindrome"
print(palindome("hello"))
print(palindome("racecar"))
print(palindome("aabaa"))



# Task 9: Sum of Squares Function

# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.


def sum_of_squares(list):
    sum = 0
    for i in list:
        sum += i ** 2
    return sum
print(sum_of_squares([1,2,3,4,5]))
print(sum_of_squares([1,2,3,4,5,6,7,8,9,10]))




# Task 10: Average Function


# Write a Python function named average that takes a list of numbers as input and returns the average value.



def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
        average = sum/len(list)
    return sum,average
print(average([1,2,3,4,5]))
print(average([1,2,3,4,5,6,7,8,9,10]))