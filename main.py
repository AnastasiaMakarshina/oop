class Shcool:
    name = "МБОУ СОШ 15"
    city = "Зеленодольск"

    def set(self, name, city):
        self.name = name
        self.city = city


gymnasium = Shcool()
gymnasium.set("Gymnasium 1", "Zelenodolsk")
print(gymnasium.name + ", " + gymnasium.city)
