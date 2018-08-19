class Shcool:
    name = "МБОУ СОШ 15"
    city = "Зеленодольск"

    def __init__(self, name, city):
        self.name = name
        self.city = city


gymnasium = Shcool("Gymnasium 1", "Zelenodolsk")
# gymnasium.set("Gymnasium 1", "Zelenodolsk")
print(gymnasium.city)


class University(Shcool):
   # inclination = technical

    def __init__(self, name, city, inclination):
        Shcool.__init__(self, name, city)
        self.inclination = inclination


KFY = University("KFY", "Kazan", inclination="technical")
print(KFY.inclination)
