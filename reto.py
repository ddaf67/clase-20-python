monto_disponible = 830
precio_celular = float(input("Ingrese la cantidad disponible: "))

if  dinero-usuario >= monto_disponible:
    cambio = monto_disponible - precio_celular
    print("El cambio a entregar es:", cambio, "soles")
else:
    print("No tienes suficiente dinero para comprar el celular.")
