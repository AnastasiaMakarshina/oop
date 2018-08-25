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

