#__name__="__main__"
def greet():
    print("hello world")

if __name__=="__main__":
    print("the script is running directly")
    greet()
#local and global variables in python
x=4
print(f"the global x is {x}")
def local():
    x=5
    print(f"the local x is {x}")
local()

#to change local variable to global
x=10
def local2():
    global x
    x=11
    y=12
    print(x)
    print(y)
local2()
print(x)
#file handling functions
#to move to a specific character in file and read the next few characters after limit
with open("log.txt","r") as f:
    f.seek(10)
    data=f.read(10)
    print(data)
#to get the current position of the cursor in file
with open("log.txt","r") as f:
    data=f.read(10)
    current_position=f.tell()
    print(current_position)
#the truncate file only writes the mentioned number of characters to the given file
with open("sample.txt","w") as f:
    f.write("hello world!")
    f.truncate(5) #writes only hello to the sample.txt file
with open("sample.txt","r") as f:
    print(f.read())
#lambda function (small anonynms function used for very small operations)
#normal function
def double(x):
    return x*(2)
print(double(5))
#using lambda function
double=lambda x : x*2
print(double(5))
cube=lambda x : x*x*x
print(cube(5))
#we can use multiple variables as well
avg=lambda x,y: (x+y)/2
print(avg(4,5))
#mostly used in high order functions
def app(fx,value):
    return 6+fx(value)
cube=lambda x : x*x*x
print(app(cube,2)) #(6+2^3)
#map, filter and reduce
#the map function applies the function to each element in the sequence and returns a new list
#normal way
l=[1,2,3,4,5]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)
#what if we try with list compressions
newl=[cube(i) for i in l]
print(newl)
#now trying using map function since cube is already made
cubel=map(cube,l)
#convert to list
cubel=list(map(cube,l))
print(cubel)
#the filter function filters elements based on a condition and returns the new list containing elements that meet the condition
l=[2,4,6,8,10]
def filter_function(a):
    return a>4
newlist=list(filter(filter_function,l))
print(newlist)
#reduce function returns the final result
from functools import reduce
num=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,num)
print(sum)
#1+2,3+3,6+4,10+5 (this is what is happening in the reduce function)
#dir function- used to get all attributes methods and functions
name=[2,4,5]
print(dir(name))
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("john",20)
print(dir(person))
#dict function- gives objects as dictionary
print(p.__dict__)
#help method is used to get documentation
print(help(person))