numero = int(input("Ingrese un numero entero positivo: "))
for i in range(numero, -1, -1):
    if i != 0:
        print(i, end=", ")
    else:
        print(i)