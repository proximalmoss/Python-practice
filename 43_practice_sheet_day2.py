#creating a dictionary
dict={"student id":1, "student name": "Hanan", "subject": "maths", "marks":65, "another dict": {"yes":"no"}, "list":[20,29,15]}
print(dict)
print(dict["student name"])
print(dict["another dict"]["yes"])
#methods/functions that can be done in dictionaries
a=dict.items()
print(a)
b=dict.keys()
print(b)
updatedict={"english":80}
c=dict.update(updatedict)
print(dict)
d=dict.get("student name")
print(d)
#all about sets
a=set({1,2,3,4,5})
print(a)
print(type(a))
print(len(a))
a.remove(2) #removes the element 2
print(a)
print(a.pop()) #removes and gives random value from set
print(a.union({6,7,8}))
print(a.intersection({3,4}))
print(a.clear())
print(a)
#extracting a specific value from the dictionary
dict={"pankha":"fan", "dabba":"box", "vastu":"item"}
print(dict)
a=input("enter the word for translation")
print("the translation is: ", dict.get(a)) #getting the value from dictionary
#finding the greatest number out of 4 numbers
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
num4= int(input("enter the fourth number: "))
if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num3):
    f2=num2
else:
    f2=num3
if(f1>f2):
    print(str(f1)+" is the greatest")
else:
    print(str(f2)+" is the greatest")
#designing a spam detector
text=input("enter a text: ")
spam=False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False
if(spam is True):
    print("this text is spam")
else:
    print(text)
#making a string as capital #makes first letter capital and makes proper
str="Harry"
str=str.capitalize()
print(str)
#while loop
i=0
while(i<5):
    print("hello")
    i+=1
#for loop
list=[15,20,29]
for i in list:
    print(i)
#for loop in range
for i in range(0,10):
    print(i)
#1-50 using while loop
i=0
while(i<=50):
    print(i)
    i+=1
#printing list of words using while loop
fruit=['banana','watermelon','grapes','mango']
i=0
while(i<len(fruit)):
    print(fruit[i])
    i+=1
#printing list of words using for loop
for i in fruit:
    print(i)
#break statement
for i in range(0,80):
    print(i)
    if i==3:
        break
#continue statement (can be used to print even and odd numbers as well)
for i in range(0,10):
    print(i)
    if(i==2):
        continue
    print(i)
#pass statement
l=[1,7,8]
for i in l:
    pass