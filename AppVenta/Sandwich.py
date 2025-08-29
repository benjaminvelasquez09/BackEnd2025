#clase padre

class Sandwich:
    def __init__(self,pan, precio):
        self.pan = pan
        self.precio = precio

    #getter
    def get_precio(self):
        return self.precio
    
    #setter
    def set_precio(self,nuevo_precio)
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

        else:
            print("el nuevo precio debe ser mayor que 0")

    def descripcion(self):
        return f"Sandwich con {self.pan}"
    

