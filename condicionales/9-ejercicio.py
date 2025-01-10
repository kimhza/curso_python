edad = int(input("Cual es tu edad? "))

if edad <= 4:
    print("La entrada es gratis")
elif edad > 4 and edad < 18:
    print("La entrada tiene un valor de $5")
else:
    print("La entrada tiene un valor de $10")