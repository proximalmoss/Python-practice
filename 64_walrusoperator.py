#allows you to assign a value to a variable within an expression
numbers=[2,4,6,8]
while (n:=len(numbers))>0:
    print(numbers.pop())
#normal way of creating a list with user without walrus
foods=list()
while True:
    food=input("what food do u like?")
    if food=='quit':
        break
    foods.append(food)
print(foods)
#using walrus operator
fruits=list()
while(fruit:=input("what fruit do u like?")) !="quit":
    fruits.append(fruit)
print(fruits)