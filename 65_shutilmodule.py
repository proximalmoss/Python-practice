#performs high level file operations
import shutil
#copies the file
shutil.copy("merged.pdf","merged2.pdf")
#copy2 is similar to copy but it preserves the metadata of the original file such as timestmap
#copytree copies the entire folder
shutil.copytree("clutter","python_images")
#to move a file from inside a folder to outside
shutil.move("python_images/Comparing MLR & SLR.png","MLR vs SLR.png")
#we cannnot delete files using shutil so we use os
import os
os.remove("img.jpg")