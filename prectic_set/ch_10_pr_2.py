class programmer:
    company="microsoft"

    def __init__(self,name,product):
        self.name=name
        self.product=product 
    def getinfo(self):
        print(f"the name is: ({self.name})")
        print(f"the  product name is: ({self.product})")
    @staticmethod
    def greet():
        print("Thank you for read my file! ")
    @staticmethod
    def time():
            print("this time is 8PM now")

    
harry=programmer("harry","Goggle")
pritesh=programmer("pritesh","Codexprt")
harry.getinfo()
pritesh.getinfo()
harry.greet()
harry.time()


