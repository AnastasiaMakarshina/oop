from universiity import *

KFY = University("KFY", "Kazan", 111, inclination="technical")
print(KFY.inclination)

result = [Shcool("Школа 22", "Зеленодольск", 22), University("IT", "Казань", 22, inclination="humanitarian")]

for shcool in result:
    shcool.display_info()
    print()
