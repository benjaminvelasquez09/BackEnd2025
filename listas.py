#diferentes formas de crear una lista

lista_vacia = []
lista_con_elementos = [1, 2, 3]
lista_con_elementos_repetidos = [0] * 5
lista_con_float = [0.0, 0.0, 0.0]
lista_con_strings = ["hola", "mundo"]
lista_mixta = [1, "hola", 3.14, True]

#bucles
# for elemento in lista_mixta:
#     print(elemento)

# for i in range(5):
#     print(i)

# while len(lista_con_elementos) > 0:
#     print(lista_con_elementos[0])
#     lista_con_elementos = lista_con_elementos[1:]


# lista_a = [1,2,3,4,5,6]
# lista_b = [4,5,6,7,8,9]

# #como  buscar elementos comunes en dos listas
# elementos_comunes = []
# for i in lista_a:
#     if i in lista_b:
#         elementos_comunes.append(i)
# print(elementos_comunes)




productos = ["laptop", "mouse", "teclado", "monitor"]
precios = [1200, 250, 80, 300]
existencias = [15, 20, 30, 20]

#debe listar todos los productos por orden y mostrar total del inventario
for i in range(len(productos)):
    print(f"productos: {productos[i]}, precios: {precios[i]}, existencias:{existencias[i]} ")
    total=precios[i]*existencias[i]
    print(f"total inventario: {total}")



    

#valor total inventario
    print("--------------------------------------")
    total_inventario = sum([precios[i] * existencias[i] for i in range(len(productos))])
    print(f"total inventario: {total_inventario}")