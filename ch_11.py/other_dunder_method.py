class number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        print("Lets add:")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets multiply:")
        return self.num* num2.num

    def __str__(self) :
        return f"Dismal number : {self.num}"



n=number(input("Enter your Dismal Number :"))
print(n)