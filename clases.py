#Las clases tienen metodos y atributos
#los atributos son sus caracteristicas
#los metodos son sus acciones

#las clases hijos pueden heredar atributos de clases padres

#necesito generar una clase con 3 atributos y 2 metodos
class autos:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Auto: {self.marca} {self.modelo}, Año: {self.año}"

    def antiguedad(self):
        return 2025 - self.año

auto1 = autos("Toyota", "Corolla", 2020)

print(auto1.descripcion())
print(f"Antigüedad: {auto1.antiguedad()} años")



