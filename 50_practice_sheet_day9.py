#docstring
def square(n):
    '''takes a number and returns square of it'''
    return n*n
print(square(5))
print(square.__doc__)
#exception handling in python
#basic try
try:
    a=int(input("enter a number"))
    print(f"multiplication table of {a}")
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
except Exception as e:
    print(e)
print("some imp lines of code")
print("end of program")
#different types of expections
try:
    x=int(input("enter an integer"))
except ValueError:
    print("number entered is not an integer")
except IndexError:
    print("Index error")
#custom errors
a=int(input("enter a number between 5 and 9"))
if(a<5 or a>9):
    raise ValueError ("enter number between 5 and 9")
a=input("Enter any value between 5 and 9. Write 'quit' to quit:")
def myfuc():
  if a=="quit":
    print("program quitted")
  else:
    if(int(a)<5 or int(a)>9):
     raise ValueError("Value should be between 5 and 9")
    else:
      print(a)
myfuc()
#enumerate function
fruits=["apple","mango","pear"]
for index,fruits in enumerate(fruits):
   print(index,fruits)
   print(f"{index+1} {fruits}")
#normal way without enumerate
marks=[12,56,32,98,12,45,14]
index=0
for mark in marks:
    print(mark)
    if(index==3):
        print("hi")
    index+=1   
#same in enumerate
marks=[12,56,32,98,12,45,14]
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("hi")