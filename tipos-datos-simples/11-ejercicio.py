cantidad = float(input("Ingresa la cantidad a invertir: "))
interes_anual = 4
for i in range(1, 4):
    futuro = (cantidad * (1 + (interes_anual/100) * i))
    print(f"Cantidad de ahorros tras año {i}: ${round(futuro, 2)}")
