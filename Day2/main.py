# def sum(a, b):
#     c = a + b
#     return c


# p = 10
# q = 15
# d = sum(p, q)

# print(d)

# def stringToDict(jstring):
    
#     jstring = jstring[1:-1]  #removed {} result : “Name”: “John Doe”,“Age”: 30,“Location”: “Dhulikhel”
#     # print(jstring)
#     replacedJstring = jstring.replace(",",":")     #“Name”: “John Doe”:“Age”: 30:“Location”: “Dhulikhel”
#     # print(replacedJstring)
#     splittedJString = replacedJstring.split(":")  # [“Name”, “John Doe”,“Age”, 30,“Location”,“Dhulikhel”]
#     # print(splittedJString)
#     print("Keys are: ")
#     print(splittedJString[::2])  #[a:b:j] 0,2,4

#     print("Values are: ")
#     print(splittedJString[1::2])

# jstr = """{“Name”: “John Doe”,“Age”: 30,“Location”: “Dhulikhel”}"""

# stringToDict(jstr)

from module1 import sum
from random import randint
a = 4
b = 5

c = sum(a, b)
# print(c)

rand = randint(0,10)
print(rand)
