suma = 0

while True:
    numero = int(input("Ingrese un numero que no sea 0: "))
    if numero == 0:
        break
    suma += numero
print("la suma es:", suma)


print("EJERCICIO 2 LISTADO DE NUMEROS")
numeros = [10, 20, 30, 40]
for i in numeros:
    print(i * 2)


print("EJERCICIO 3 LISTADO DE NUMEROS")

productos =[]
for i in range(3):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("stock: "))
    producto = {"nombre":  nombre, "precio": precio, "stock": stock}
    productos.append(producto)

for x in productos:
   print(f"{x['nombre']}: Q{x['precio']} ({x['stock']} disponibles)")