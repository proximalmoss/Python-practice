#printing multiplication table using for loop
n=int(input("enter a number: "))
for i in range (0,11):
    print (str(i)+"x"+str(n)+"= "+str(i*n))
#trying startswith function
l=["Harry","Simon","Sam","Ethan"]
for i in l:
    if i.startswith("S"):
        print("Hello "+i)
#trying multiplication with while loop
num=int(input("enter a number"))
i=1
while(i<11):
    print (str(i)+"x"+str(num)+"= "+str(i*num))
    i+=1
#Checking if a number is prime
x=int(input("enter a number"))
prime=True
for i in range (2,x):
    if(x%i==0 and x!=2):
        prime=False
        break
if(prime is True):
    print("The number is prime")
else:
    print("The number is not prime")
#finding the sum of n natural numbers using while loop
y=int(input("enter a number"))
sum=0
i=0
while(i<=y):
    sum=sum+i
    i+=1
print("sum= "+str(sum))
#Calculating the factorial of a number
n1=int(input("enter a number"))
fact=1
for i in range(1,i+1):
    fact=fact*i
print(f"the factorial of {n1}= {fact}")
#printing pattern
n=5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
#triangle pattern
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
#reverse triangle pattern
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print()
#right sided triangle
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range (i+1):
        print("*", end=" ")
    print()
#upside down right triangle
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*", end=" ")
    print()
#printing proper triangle
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range (i+1):
        print("*",end=" ")
    print()
#printing upside down triangle
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
#when combining the top two give the diamond pattern
#printing good day using a function and we take input from user
def func():
    name=input("enter your name")
    print("hello! "+name)
func()
#printing good day using function but we enter the name
def func1(name1):
    print("hello "+name1)
func1("hanan")
#printing good day using function but we use defauly argument
#in case value is not entered the function will print with default arguament
def func2(name2="Stranger"):
    print("hello "+ name2)
func2("Hanan")
func2()
#finding factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n+factorial(n-1)
print(factorial(5))