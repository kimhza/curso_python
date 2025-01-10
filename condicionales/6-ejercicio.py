nombre = input("Cual es tu nombre?: ")
sexo = input("Cual es tu sexo (M o H)? ")

if (sexo == "M" and nombre[0].lower() < "m") or (sexo == "H" and nombre[0].lower() > "n"):
    print(f"{nombre} pertences a Grupo A")
else:
    print(f"{nombre} pertences a Grupo B")
