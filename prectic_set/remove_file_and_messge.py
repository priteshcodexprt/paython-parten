import os



Filename=input("Enter the remove file name :")

if os.path.exists(Filename):
    os.remove(Filename)
    print("This file is found and remove!")

else:
    print("THis file is not found ")