#variables #Variables are containers to store any data
name = "Ranjan"
print(name)
name = 100  #A single variable can be reassigned multiple times
print(name)

name, age, location = "Ranjan", 22, "Dhulikhel"  #Multiple variable can be declared
print(name, age, location)

program = "Python"
value = 100
print(type(value))

#Type Function gives the Data type of the variable
#There are several Data types in python 

value = str(100)
print(type(value))   
programValue = program + value
print(programValue)
print(type(programValue))


#Data Types

#Numeric Data Types
var1 = 100  #Integer Data Type
var2 = 100.00 #Float Data Type

var3 = complex(4, 5)  #Complex Data Type

print(type(var1))
print(type(var2))
print(type(var3))


#String
#String is a sequence of characters
string1 = 'hello'
string2 = "world"
string3 = '''hello  
world''' #multiline string

print(string1, string2, string3)

#Indexing a string
#Index of a string start at 0 as first character and -1 as last character
string1 = 'Django WebApp'
#   index  0123456789...

print(string1[0])  #0th index or first character inside ""
print(string1[-1])  #-1th index or last character inside ""

#String Slicing
#We can slice any string by mentioning the first character and n+1 th character 
print(string1[1:6])  # gives index 1 to 5
print(string1[:6])   # gives index 0 to 5

print(string1[:])  #gives index of first character to last character


##lower, upper
string1 = string1.lower() #converts into lowercase string
print(string1)

string1 = string1.upper() #converts into uppercase string
print(string1)

##split
#SPLIT function can be used to split or break a string into multiple strings
#it gives output as list of broken strings

strlist = string1.split(" ") #Spliting in reference to " " a white space
print(strlist)

string = "a,b,a, b,c:d,e,f"

srtlist = string.split(",") #splitting in reference to ","
print(srtlist)

srtlist = string.split(":") #splitting in reference to ":"
print(srtlist)

# #find function returns the first occurance of the character or string
print(string.find("a, "))



#Replace function
#Replaces the first occurance of the specified character to given character
string3 = "Kathmandu University"
string3 = string3.replace("K", "L")

print(string3)


# list
# List is a sequential data type that hold a list of anythig.
#We can create a list of different datatypes in a single list

#list of integers
listXYZ = [1, 2, 3, 400, 1, 2, 3]

print(type(listXYZ))

print(listXYZ)


# list of mixed data types
list2 = [1,2, "KU", 1.0001, complex(2, 3)]
print(list2)

list3 = [1,2, ['a', 'b','c'],"ranjan"]

# print(list3[0])
# print(list3[2])

#Append function adds given elements to last of list
list3.append(1000)
print(list3)


#Insert function adds given elements to specified index in list
list3.insert(1, "KU")
print(list3)

#POp function removes element from last of list
list3.pop()
list3.pop(0)
print(list3)

#Remove function removes specified element from list
list3.remove("KU")
print(list3)

#Reverse function reverses list
list3.reverse()
print(list3)

#Clear function removes every element from list
list3.clear()
print(list3)

####List can be indexed as string


##SET DATA Type
#Set is an unordered data type,of sequence of difq elements. Set cannot be indexed
#Set cannot contain duplicates
#Set is defined by curly brackets

set1 = set(["a", "b", "c", "d", "e"])
print(type(set1))
print(set1)

set2 = {"KU", 100}

# Update function adds the specified items into set. 
#Here we are updating the set with the list of items so the items not are added individually to set
#But if we add the same list using add function , the whole list is added to the set as a single element
set2.update([1,2,3])
print(set2)

set2.add(1)
print(set2)

#pop function removes the first item from set
set2.pop()
print(set2)

#Remove function removes the specified item from set
set2.remove(2)
print(set2)



##DIctionary
#Dictionary is a datatype in which the elemens exists in pairs or "key" and "value"
#for each keys values must be passed
#keys and values can be of any data type including dictionary itself
dict1 = {
    "Name":"KU",
    "location":"Dhulikhel",
    "estd": 1997,
    "Departments": ["CE", "Civil", "Mech"],
    "something": {"s1":1, "S2":2},
}

print(type(dict1))

#We can asscess the value of any key of dictionary by passing the key in square brackets
print(dict1["Name"])

#We can update the value of any key of dictionary assigning as follows
dict1["Name22"] = "TU"

#Similarly we can create a new pair of key and value by same above code


print(dict1)

#Question 1
jstring = """{“Name”: “John Doe”,“Age”: 30,“Location”: “Dhulikhel”}"""
jstring = jstring[1:-1]
print(jstring)
replacedJstring = jstring.replace(",",":")
print(replacedJstring)
splittedJString = replacedJstring.split(":")
print(splittedJString)
print("Keys are: ")
print(splittedJString[::2])

print("Values are: ")
print(splittedJString[1::2])