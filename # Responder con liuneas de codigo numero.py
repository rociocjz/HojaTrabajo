suma = 0

while True:
    numero = int(input("Ingrese un numero que no sea 0: "))
    if numero == 0:
        break
    suma += numero
print("la suma es:", suma)