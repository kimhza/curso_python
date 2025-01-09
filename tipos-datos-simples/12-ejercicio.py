precio_barra = 3.49
dcto_pan = 0.6
barras = int(input("Ingrese el número de barras vendidas: "))
precio_total = round((barras * precio_barra), 2)
precio_no_fresco = round((precio_total * dcto_pan), 2) 
print(f"El precio habitual de una barra de pan es ${precio_barra}")
print(f"El precio con descuento es: ${precio_no_fresco}")
print(f"El precio total es: ${precio_total}")