#generators are special type of function that allow to create an iterable source of values
#yield keyword gives a value from the generator on request and suspends until the next value is requested again
def my_generator():
    for i in range(5):
        yield i
gen=my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#this is because generator generates value on the fly
#this saves memory unlike the for loop

#now if i want to do as usual
for j in gen:
    print(j)