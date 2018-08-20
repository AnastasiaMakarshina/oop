class Shcool:
    name = "МБОУ СОШ 15"
    city = "Зеленодольск"
    age = 200

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    def display_info(self):
        print("Название:", self.name, ", ", "возраст:", self.age)


# gymnasium = Shcool("Gymфasium 1", "Zelenodolsk", 122)
# print(gymnasium.city)


class University(Shcool):

    def __init__(self, name, city, age, inclination):
        Shcool.__init__(self, name, city, age)
        self.inclination = inclination

    def display_info(self):
        print("Университет", self.name, "город", self.city)


KFY = University("KFY", "Kazan", 111, inclination="technical")
print(KFY.inclination)

result = [Shcool("Школа 22", "Зеленодольск", 22), University("IT", "Казань", 22, inclination="humanitarian")]

for shcool in result:
    shcool.display_info()
    print()
