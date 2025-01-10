edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))

if edad > 16 and salario >= 1000:
    print("Debe tributar")
else:
    print("El usuario no debe tributar.")