from shcool import *

class University(Shcool):

    def __init__(self, name, city, age, inclination):
        Shcool.__init__(self, name, city, age)
        self.inclination = inclination

    def display_info(self):
        print("Университет", self.name, "город", self.city)

KFY = University("KFY", "Kazan", 111, inclination="technical")
print(KFY.inclination)