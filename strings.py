
#Coding Exercises

#You are given a string sentence.print the characters at even indices:

sentence = "python is amazing"
empty_str = ""
for i in range(len(sentence)):
    # print(sentence[i],i)
    if i %2 == 0:
        empty_str += sentence[i]
print(empty_str)




#You are given a string s. Replace all spaces in the string with underscores(_) and prin the modified string


s = "python is fun and powerful"
for i in range(len(s)):
    if s[i].isalpha():
        print(s[i],end = "")
    else:
        print("_",end = "")



# You are given a string s. Check if the string contains only digits

s = "12345"
contains = s.isnumeric()
print(contains)



#You are given a string s. Print the string in reverse order

s = "python is amazing"
print(s[-1::-1])


s = "python is amazing"
reverse_str = ""
for i in range(len(s)-1,-1,-1):
    reverse_str += s[i]
print(reverse_str)



#You are given a string s.capitalize the first letter of each word in the string and print the modified string

s = "python programming is fun"
capitalize = s.title()
print(capitalize)