producto = input("Escribe el nombre del producto: ")
precio = float(input("Ingresa el precio del producto: "))
unidades = int(input("Ingrese el numero de unidades del producto: "))

print(f"Producto {producto}, {unidades:3d} unidades, precio unitario ${precio:9.2f}, costo total ${(precio*unidades):11.2f}")
