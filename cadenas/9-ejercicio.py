birthdate = input("Ingresa fecha de nacimiento (dd/mm/aaaa)")
dia = birthdate[:birthdate.find("/")]
mes_año = birthdate[birthdate.find("/") +1:]
mes = mes_año[:mes_año.find("/")]
año = mes_año[mes_año.find("/")+ 1:]
print(f"Dia: {dia}, Mes: {mes}, Año: {año}")