#STONE PAPER SCISSOR GAME 

import random
def game(comp,you):
    if (comp==you):
        return None
    elif (comp=="st"):
        if you=="p":
            return True
        elif you=="sc":
            return False
    elif (comp=="p"):
        if you=="sc":
            return True
        elif you=="st":
            return False
    else:
        if you=="st":
            return True
        elif you=="p":
            return False
print("computer's turn: stone(st), paper(p), scissor(sc)")
randno=random.randint(1,3)
if randno==1:
    comp="st"
elif randno==2:
    comp="p"
else:
    comp="sc"
you=input("your turn: stone(st), paper(p), scissor(sc)")
a=game(you,comp)
print(f"computer chose {comp}")
print(f"you chose {you}")
if(a==None):
    print("DRAW!")
elif(a==False):
    print("YOU WIN!")
else:
    print("you lose,better luck next time...")

#files in python
file=open("file.txt","w")
file.write("This is a text file made for practice")
file.close()
#To check whether the word twinkle is present in the file
file1=open("twinkle.txt","r")
twinkle=file1.read()
if "twinkle" in twinkle:
    print("Twinkle is present in file")
else:
    print("Twinkle is not present in file")
file1.close()
#to replace the word donkey in file
with open("file.txt","r") as file2:
    content=file2.read()
    content=content.replace("donkey","$#%&")
with open("file.txt","w") as file2:
    content=file2.write(content)
#copying a text file
with open ("log.txt","r") as original:
    text=original.read()
with open ("copy.txt","w") as original:
    original.write(text)
#checking if two files are same
with open("log.txt","r") as f:
    f1=f.read()
with open("copy.txt","r") as f:
    f2=f.read()
if (f1==f2):
    print("the two files are same")
else:
    print("the two files are not same")
#renaming file
import os
with open("copy.txt","r") as f:
    x=f.read()
with open("renamed.txt","w") as f:
    f.write(x)
os.remove("copy.txt")
#tracking highscore of game using file
def game():
    return 5 
score=game()
with open("highscore.txt") as f:
    highscore=int(f.read())

if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))
#mining a logfile and checking if it has the word python
with open("log.txt","r") as f:
    content=f.read()
if "python" in content.lower():
    print("python is present")
else:
    print("python is not present")
#now checking which line python is present in
content=True
i=1
with open("log.txt","r") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(f"python is present is line {i}")
        i+=1