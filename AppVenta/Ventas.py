from Sandwich import Sandwich
class Venta:
    def __init__(self):
        self.pedidos = []

    def agregar_sandwich(self,sandwich):
        print(f"Agregado {sandwich.descripcion()}  - precio: {sandwich.get_precio()}")
        self.pedidos.append(sandwich)

    def mostrar_ventas(self):
        print("--------Resumen de la venta------")
        total = 0
        for s in self.pedidos:
            print(f"{s.descripcion()}   |  {s.get_precio()}")
            total += s.get_precio()
              
        print(f"Total a pagar: {total}")





