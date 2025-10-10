#patterns
n=5
#Q1
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
#Q2
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#Q3
for i in range(n+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print()
#Q4
for i in range(n+1):
    for j in range(1,i+1):
        print(f"{i}",end=" ")
    print()
#Q5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
#Q6
for i in range(1,n+1):
    for j in range(i,n+1):
        print(f"{j}",end=" ")
    print()
#Q7
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
#Q8
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
#Q9
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
#Q10
for i in range((2*n)-1):
    if i<n:
        for j in range(i+1):
            print("*",end=" ")
    else:
        for j in range(2*n-i-1):
            print("*",end=" ")
    print()
#Q11
for i in range(n):
    start=1
    if i%2==0:
        start=1
    else:
        start=0
    for j in range(i+1):
        print(f"{start}",end=" ")
        start=1-start
    print()
#Q12
spaces=2*(n-1)
#left
for i in range(1,n+1):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
#space
    for j in range(spaces):
        print(" ",end=" ")
#right
    for j in range(i,0,-1):
        print(f"{j}",end=" ")
    print()
    spaces-=2
#Q13
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
#Q14
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+j),end=" ")
    print()
#Q15
for i in range(n):
    for j in range(i,n):
        print(chr(ord('A')+j),end=" ")
    print()
#Q16
for i in range(n):
    for j in range(i+1):
        print(chr(ord('A')+i),end=" ")
    print()
#Q17
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(ord('A')+j),end=" ")
    for j in range(i-1,-1,-1):
        print(chr(ord('A')+j),end=" ")
    print()
#Q18
for i in range(n):
    for j in range(n-i-1,n):
        print(chr(ord('A')+j),end=" ")
    print()
#Q19
spaces=0
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(0,spaces):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    spaces+=2
    print()
spaces=2*(n-1)
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(spaces):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    spaces-=2
    print()
#Q20
spaces=2*n-2
for i in range(1,2*n):
    stars=i
    if i>n:
        stars=2*n-i
    for j in range(stars):
        print("*",end=" ")
    for j in range(spaces):
        print(" ",end=" ")
    for j in range(stars):
        print("*",end=" ")
    print()
    if i<n:
        spaces-=2
    else:
        spaces+=2
#Q21
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#Q22
size=2*n-1
for i in range(size):
    for j in range(size):
        top=i
        left=j
        bottom=size-1-i
        right=size-1-j

        val=n-min(min(top,bottom),min(left,right))
        print(val,end=" ")
    print()