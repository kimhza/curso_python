num_tel = input("Escribe el numero de telefono completo: ")
prefijo = num_tel[:3]
numero = num_tel[4:-3]
extension = num_tel[-2:]
print(f"""INFORMACIÓN TELEFONICA:
* Prefijo: {prefijo}
* Número: {numero}
* Extensión: {extension}""")