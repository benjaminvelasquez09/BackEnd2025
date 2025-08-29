from Sandwich import Sandwich
from Ventas import Venta
from Sandwich_Vegetariano import Sandwich_vegetariano

# Crea el objeto del sándwich
mi_sandwich = Sandwich_vegetariano("pan de ajo", 1500, "tomate")
print(mi_sandwich.descripcion())

# Crea una instancia de la clase Venta
mi_venta = Venta()

# Agrega el sándwich a la venta
mi_venta.agregar_sandwich(mi_sandwich)

# Llama al método para mostrar las ventas (sin argumentos)
mi_venta.mostrar_ventas()