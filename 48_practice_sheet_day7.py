#single inheritance
class employee:
    company="google"
    def showdetails(self):
        print("this is an employee")
class programmer(employee):
    def getlanguage(self,language):
        self.language=language
        print(f"the langauge is {self.language}")
    def showdetails(self):
        print("this is a programmer")
e=employee()
p=programmer()
e.showdetails()
p.showdetails()
p.getlanguage("python")
print(p.company)
#Multiple inheritance
class Employee:
    company="Visa"
    ecode=12
class Freelancer:
    company="Fiverr"
    level=0 #you only need an intial value for attribute in self
    def upgradeLevel(self):
        self.level=self.level+1
class Programmer(Employee,Freelancer): 
#if we reverse this company will be Fiverr becuause priority is given according to the order you write
    name="Rohit"
p=Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)
#multilevel inheritance
class Person:
    country="India"
    def takeBreak(self):
        print("I am breathing")
class Employee(Person):
    company="Honda"
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreak(self):
        print("I am an employee so I am breathing")
class Programmer(Employee):
    company="Fiverr"
    def getSalary(self):
        print("no salary programmer")
#super() method
    def takeBreak(self):
        super().takeBreak()
        print("I am programmer so I breath")
p=Person()
e=Employee()
pr=Programmer()
p.takeBreak()
e.takeBreak()
pr.takeBreak()
#class method
class employee():
    company="google"
    salary="100"
    def changesalary(self,salary):
        self.__class__.salary=salary
e=employee()
print(e.salary)
e.changesalary(455)
print(e.salary) #changes salary directly in the class
#property decorators
class employee:
    company="bharat gas"
    salary=500
    bonus=100
    totalsalary=600
    @property
    def totalsalary(self):
        return self.salary+self.bonus
    @totalsalary.setter
    def totalsalary(self,value):
        self.bonus=value-self.salary
e=employee()
print(e.salary)
print(e.bonus)
print(e.totalsalary)
e.bonus=700
print(e.totalsalary)
e.totalsalary=6100
print(e.bonus)
#operator overloading
class number:
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,num2):
        return self.num1+num2.num1
n1=number(4)
n2=number(6)
sum=n1+n2
print(sum)
#class to take in 2D and 3D vectors
class C2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
class C3dvec(C2dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
v2d=C2dvec(3,4)
v3d=C3dvec(5,7,10)
print(v2d)
print(v3d)
#using static method
class Animals:
    animaltype="mammal"
class Pets(Animals):
    color="white"
class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")
d=Dog()
d.bark()
#getter and setter for salary and increment
class Employee:
    salary=1000
    increment=1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary
e=Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement=2000
print(e.increment)
#creating class for complex numbers adding and multiplying
class complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i
    def __add__(self,c):
        return complex(self.real+c.real,self.img+c.img)
    def __str__(self):
        if self.img<0:
            return f"{self.real} - {-self.img}i"
        else:
            return f"{self.real} + {self.img}i"
    def __mul__(self,c):
        mulreal= self.real*c.real-self.img*c.img
        mulimg=self.real*c.img+self.img*c.real
        return complex(mulreal,mulimg)
c1=complex(1,4)
c2=complex(3,5)
print(c1+c2)
print(c1*c2)