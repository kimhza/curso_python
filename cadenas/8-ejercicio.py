precio = input("Ingresa precio del producto con 2 decimales: ")
valor_sep = precio.split(".")
euros = valor_sep[0]
centimos = valor_sep[1]
print(f"Euros: {euros}, centimos: {centimos}")