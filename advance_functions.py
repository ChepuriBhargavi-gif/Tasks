
# Coding exercises:

# Write a Python function 
# square_all(numbers) that takes a list of numbers as input 
# and returns a new list containing the square of each number in the input list. 
# Use the map() function with a lambda function to implement this.



list_2 = [1,2,3,4,5]
result = map(lambda a : a ** 2,list_2)
print(list(result))


# Write a Python function filter_positive(numbers) that takes a list of numbers as 
# input and returns a new list containing only the positive numbers from the 
# input list. Use the filter() function with a lambda function to implement this.



list_1 = [1,2,3,-4,10,-20,33,22]
result = filter(lambda a : a > 0 , list_1)
print(list(result))



# Write a Python function calculate_factorial(n) that calculates the factorial of a 
# given number n. Use the reduce() function with an appropriate lambda 
# function to implement this.


def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(fact(5))


# Write a Python function count_vowels(string) that takes a string as input and 
# returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() 
# function with an appropriate lambda function to implement this.




def count_vowels(str):
    count = 0
    for i in str:
        if i in "aeiou":
            count += 1
    
    return count

print(count_vowels("hello"))