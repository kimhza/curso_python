clave_inicial = "contraseña"
clave_usuario = input("Ingresa una contraseña: ")
if clave_usuario.lower() == clave_inicial.lower():
    print("La contraseña coincide con la contraseña inicial.")
else:
    print("La contraseña no coincide.")