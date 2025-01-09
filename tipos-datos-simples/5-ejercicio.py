usuario = input("Cual es tu nombre? ")
horas = int(input("Cuantas horas trabajaste? "))
coste_hora = int(input("Cual es el costo por hora? "))
pago = horas * coste_hora
print(f"{usuario}, tu pago es ${pago}")