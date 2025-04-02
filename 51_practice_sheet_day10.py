#short hand for if statements- used when the if condition is short
#normal way
a=303
b=3033
if a>b:
    print("A")
elif(a==b):
    print("=")
else:
    print("B")
#using short hand
print("A") if a>b else print ("=") if a==b else print ("B")
#we can also give expressions
c=9 if a>b else 0 
print (c)