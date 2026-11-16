#coding questions

# problem1 : using break in a while loop

numbers = [25,30,20,40,15,25]
sum = 0
for i in numbers:
    sum += i
    if sum >= 100:
        break

# print(f"Sum is exceeded")
    

numbers = [25,30,20,40,15,25]
sum = 0
for i in numbers:
    sum += i
    print(i)
    if sum >= 100:
        break

print(f"sum is exceeded {i}")



# problem2 : using numbers in a loop


for i in range(1,601):
    if i %2 == 0:
        continue
    
    print(i)


#problem3 : using pass in conditional statements


for i in range(11):
    if i %2 == 0:
        print("Even")
    else:
        pass


#problem4 : 


words = ["apple","banana","break","tv","fridge","skip","dragon","mango"]

for i in words:

    if i == "skip":
        continue
    elif i == "break":
        break
    else:
        print(i)