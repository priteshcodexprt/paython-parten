class number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        print("Lets add:")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets multiply:")
        return self.num* num2.num
    
    def __sub__(self,num2):
        print("Lets sub:")
        return self.num - num2.num


    def __truediv__(self,num2):
        print("Lets truediv:")
        return self.num / num2.num

    def __floordiv__(self,num2):
        print("Lets floordiv:")
        return self.num // num2.num


n1=number(499)
n2=number(685)


sum=n1+n2
print(sum)


mul=n1*n2
print(mul)


sub=n1-n2
print(sub)
truediv= n1/n2
print(truediv)
floordiv= n1//n2
print(floordiv)
