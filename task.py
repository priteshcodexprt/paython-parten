from fileinput import filename
import os
filename=input("Enter your file name:")

if os.path.exists(filename):
  os.remove(filename)
else:
  print("The file does not exist") 