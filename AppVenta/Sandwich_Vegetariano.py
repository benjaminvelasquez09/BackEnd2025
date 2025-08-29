from Sandwich import Sandwich

class Sandwich_vegetariano(Sandwich):

    def __init__(self, pan, precio, verduras):
        super().__init__(pan, precio)
        self.verduras = verduras

    def descripcion(self):
        return f"Sandwich vegetariano con {self.pan} y {self.verduras}"



