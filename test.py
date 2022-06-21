import os


oldFilename= (input("Enter your oldFilename :"))
newFilename=(input("Enter your new file name :"))
with open (oldFilename) as f:
    
    content = f.read()


with open (newFilename,'w') as f:
    f.write(content)

    os.remove(oldFilename)