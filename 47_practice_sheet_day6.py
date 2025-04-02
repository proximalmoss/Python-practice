#class attribute and instance attribute
class employee:
    company="Google"
    salary=100
harry=employee()
ethan=employee()
print(harry.salary)
print(ethan.salary)
harry.salary=30
print(harry.salary)
print(ethan.salary)
#self parameter
class employee:
    company="Google"
    def getSalary(self):
        print("salary is 100K")
harry=employee()
harry.getSalary()
employee.getSalary(harry)
#in the self function if we want to add the salary outside the class
class employee:
    company="google"
    def getSalary(self):
        print(f"salary is {self.salary}")
        print(f"company is {self.company}")
harry=employee()
harry.salary=100
harry.company="yt"
#First priority is always given to the instance attribute, in case the instance attribute is not given only then class attribute is given
harry.getSalary()
#static method
class hi:
    @staticmethod
    def greet():
        print("good morning")
harry=hi()
harry.greet()
hi.greet()
#__init__constructor
#used to run the method without being called
class employee:
    def __init__(self):
        print("employee is created!")
harry=employee()
#now using it in an actual question
class employee:
    team="dev"
    def __init__(self,company,salary):
        self.company=company
        self.salary=salary
        print("employee is created")
    def details(self):
        print(f"company: {self.company}")
        print(f"salary: {self.salary}")
        print(f"team: {self.team}")
harry=employee("google","100k")
harry.details()
#class to find square, square root and cube of a number adn with static method to greet user
class calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"square is {self.number**2}")
    def squareroot(self):
        print(f"sqaureroot is {self.number**0.5}")
    def cube(self):
        print(f"cube is {self.number**3}")
    @staticmethod
    def greet():
        print("hello! welcome to calculator")
calculator.greet()
n=int(input("enter number: "))
o=int(input("choose option 1.SQAURE 2.SQUAREROOT 3.CUBE"))
a=calculator(n)
if o==1:
    a.square()
elif o==2:
    a.squareroot()
elif o==3:
    a.cube()
else:
    print("invalud input")
#creating a class of train and booking a train ticket
class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"name of train: {self.name}")
        print(f"number of seats available: {self.seats}")
    def getFare(self):
        print(f"fare: {self.fare}")
    def bookTicket(self):
        if self.seats>0:
            print(f"ticket has been booked! your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry this train is full...")
intercity=train("intercity express:1120",90,300)
intercity.getStatus()
intercity.bookTicket()
intercity.bookTicket()