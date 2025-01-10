puntuacion = float(input("Indica tu nivel de rendimiento: "))

if puntuacion in [0, 0.4, 0.6] or puntuacion > 0.6:
    dinero = 2400 * puntuacion

print(f"Tu nivel de rendimiento es {puntuacion} y la cantidad de dinero que recibirás es {dinero}")
