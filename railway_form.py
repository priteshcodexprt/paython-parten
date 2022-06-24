class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"train name is: {self.train}\nname is: {self.name}")
harryAppliCation= RailwayForm()
harryAppliCation.name="Harry"
harryAppliCation.train="Rajdhani Express"
harryAppliCation.printData()