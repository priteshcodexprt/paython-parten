name = input("Enter your name : ")
a = len(name)
print("length of this name is " + str(a))
if(a<10):
    print("The name contains less than 10 characters")
elif(a==10):
    print("The name contains exactly 10 characters")
else:
    print("The name contains more than 10 characters")