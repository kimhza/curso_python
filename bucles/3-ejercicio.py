numero = int(input("Ingresa un numero entero positivo: "))
for i in range(1, numero+1):
    if i %2 != 0:
        print(f"Numero impar {i}")