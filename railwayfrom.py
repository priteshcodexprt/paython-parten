class RailwayForm :
    formType="RailwayFrom"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

HarryApplication=RailwayForm()
HarryApplication.name=("Harry")
HarryApplication.train=("Rajdhani Express")
HarryApplication.printData()
