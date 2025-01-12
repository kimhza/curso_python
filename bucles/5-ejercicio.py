cantidad = float(input("Ingrese una cantidad a invertir: "))
interes_anual = float(input("Ingrese un interes anual: "))
años = int(input("Ingrese el número de años: "))

for i in range(1, años + 1):
    cantidad *= 1 + interes_anual / 100
    print(f"Capital al finalizar año {i}: ${round(cantidad, 2)}")