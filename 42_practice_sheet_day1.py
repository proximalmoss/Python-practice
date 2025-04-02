#printing a string
print ("starting my practice today")
#printing a list of all the files in the folder
import os
print(os.listdir())
#printing the variable and its types
a=69
print(a)
print(type(a))
#adding 2 variables and adding number to a variable directly
a=69
b=31
print(a+b)
b+=4
print(b)
#boolean values
print(69<143)
bool1=True
bool2=False
print (bool1 and bool2)
print (bool1 or bool2)
print (not bool1)
#taking input from user and changing the dtype of the number
d=input("enter a number")
print (d) #converting
d=float(d)
print(d)
#concating 2 strings in python
n1="Hello, "
n2="Hanan"
print (n1+n2)
#getting required elements from string or slicing string through index
print(n1[4])
print(n1[:3])
print(n1[0:])
print(n1[1:3])
print(n1[-1])
#getting length of string
print(len(n1))
#counting the number of times a specific character appears
n2=n2.count("n")
print(n2)
#replacing characters in a string
s1="this is a string with double  spaces"
doublespace=s1.find("  ") #returns index of the reqd character
singlespace=s1.replace("  ", " ")
print(doublespace)
print(singlespace)
#All about lists
L1=[2,4,6,8,10]
L1.sort()
print(L1)
L1.append(20)
print(L1)
L1.reverse()
print(L1)
L1.insert(3,1) #inserts element in index 3
print(L1)
L1.pop(2) #removes element from index 2
print(L1)
L1.remove(10) #removes the specified element
print(L1)
#All about tuples
a=()
b=(1,)
c=(1,2,3)
c=c.count(2) #counts the number of times 2 occurs in the tuple
print(c)
print(b.index(1)) #gives index of the specified element