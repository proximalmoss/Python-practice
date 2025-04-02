#function to print the greatest of 3 numbers
def great():
    num1=int(input("enter the first number: "))
    num2=int(input("enter the second number: "))
    num3=int(input("enter the third number: "))
    if (num1>num2 and num1>num3):
        return str(num1) + "is greatest"
    elif(num2>num1 and num2>num3):
        return str(num2) + "is greatest"
    else:
        return str(num3) + "is greatest"
print(great())
#another way where we can enter values after making the funtion and not asking user
def max(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif (num2>num1 and num2>num3):
        return num2
    else:
        return num3
m=max(3,5,7)
print("gratest number is "+ str(m))
#converting celsius to fharenheit
def temp(c):
    temprature=(c*9/5)+32
    return temprature
f=temp(0)
print("the temprature in fharenheit is: " + str(f))
#recursive funtion to calculate the sum of n natural numbers
def sum (n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(1))
#funtion to print pattern
def pattern(x):
    for i in range(x):
        for j in range(i+1):
            print("*", end=" ")
        print()
pattern(5)
#function to strip and remove word from string GIVING LIST 
def remove (string,word):
    newstr=string.replace(word,"")
    return newstr.strip() #only removes spaces from front and end
s="   Hanan is   good"
n=remove(s,"Hanan")
print(str(n))
#function to print multiplication table
def multiplication(n1):
    for i in range(1,11):
        product=n1*1
        print (f"{i} x {n1} = {product}")
multiplication(5)