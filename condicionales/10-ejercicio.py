tipo_pizza = ["Vegetariana", "No Vegetariana"]
pizza_vegetariana = ["Pimiento", "Tofu"]
pizza_no_vegetariana = ["Peperoni", "Jamón", "Salmón"]

sel_pizza = int(input("Escribe 0: Pizza Vegetariana ó 1: Pizza No Vegetariana"))
pizza = tipo_pizza[sel_pizza]

if sel_pizza == tipo_pizza[sel_pizza]:
    ingredientes = pizza_vegetariana
else:
    ingredientes = pizza_no_vegetariana

print(f"La pizza seleccionada es {pizza} y tiene estos ingredientes {str(ingredientes)}")
