import os


oldFilename=input("Enter your olFilename :")
newFilename=input("Enter your newFilename :")

with open (oldFilename) as f:
    content=f.read()

with open (newFilename,'w') as f:
    f.write(content)

os.remove(oldFilename)