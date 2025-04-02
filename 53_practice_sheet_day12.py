#more file related dunctions
with open ("twinkle.txt", "r") as f:
    while True:
        line=f.readline()
        print(line)
        if not line:
            print(line,type(line))
            break
#splitting marks of student
with open ("twinkle.txt", "r") as f:
    i=0
    while True:
        i+=1
        line=f.readline()
        if not line:
            break
        m1=line.split(",")[0]
        m2=line.split(",")[1]
        m3=line.split(",")[2]
        print(f"marks of student {i} in math is {m1}")
        print(f"marks of student {i} in science is {m2}")
        print(f"marks of student {i} in english is {m3}")