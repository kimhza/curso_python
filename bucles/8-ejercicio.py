numero = int(input("Ingrese un numero entero positivo: "))

for i in range(1, numero + 1):
    if i % 2 != 0:
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")
