class programmer:
        company="Microsoft"

        def __init__(self,name,product):
                self.name=name
                self.product=product

        def getinfo(self):
                print(f"The name is {self.name} This product name is {self.product}")

harry=programmer("harry","skype")
alka=programmer("alka","Goggle")
harry.getinfo()
alka.getinfo()
