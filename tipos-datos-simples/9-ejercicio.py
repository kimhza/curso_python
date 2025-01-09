cantidad = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interes anual: "))
agnos = int(input("Indica el número de años: "))
cap_futuro = (cantidad * (1 + (interes_anual/100) * agnos)) - cantidad 
print(f"El capital obtenido por ${cantidad}, a una tasa anual de {interes_anual}% durante {agnos} años es: ${cap_futuro}")