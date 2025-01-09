peso = float(input("Cual es tu peso (Kg)?: "))
estatura = float(input("Cual es tu altura (metros)?: "))
imc = round((peso / (estatura ** 2)), 2)
print(f"Tu índice de masa corporal es: {imc}")