##INPUT FUNCTION
#Input fuction asks input from user in terminal

age = input("Enter your age:")

print(f"You are {age} yours old") #Search for fstring in google. Its interesting


#IF-ELSE
"""If else statements are needed if we want our code to take dicisions based
on the condition given.
If a condition is true then the code in if is executed otherwise the code
in else is executed
"""
a = input("Enter your age:")
if int(a) >= 18:
    print("You are adult")
else:
    print("You are kid")

#Similarly if we have more than 2 conditions we use if-elif-else
#IF-ELIF-ELSE
a = input("Enter your age:")
if int(a) > 18:
    print("You are adult")

elif int(a) == 18:
    print("You are 18")

else:
    print("You are kid")


##Nested IF/ELSE
a = input("Enter your age:")
if int(a) >= 18:
    if int(a) == 18:
        print("You are exactly 18")
    else:
        print("You are older than 18")

else:
    print("You are  under 18")


#FOR LOOOP
"""
Python For loop is used for sequential traversal i.e.
 it is used for iterating over an iterable like String, Tuple, List, Set or Dictionary.
In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). 
There is “for” loop which is similar to each loop in other languages.
Note: In Python, for loops only implements the collection-based iteration.
"""
no = int(input("number:"))
for i in range(no):
    print("Hello, world")

list = ['a', 'b', 'c', 'd', 'e', 'f']

for i in list:
    print(f"Hello {i}")


#WHILE LOOP
"""
Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.
And when the condition becomes false, the line immediately after the loop in the program is executed.
"""
a = 5

while (a < 10):
    a += 1
    if a == 7:
        continue
    print("Hello World")
    if a == 8:
        break

#Search for break and continue 