nota = float(input("Ingresa tu nota: "))

if nota == 20:
    print("como",nota," es tu nota,te comprare una pc")
elif  nota >= 0 and nota <=18:
    print("como",nota," es tu nota,te comprare un celular")
elif  nota >= 0 and nota <=16:
    print("como",nota," es tu nota,te comprare una tarjeta de dinero")
elif  nota >= 0 and nota <=12:
   print("como",nota," es tu nota,te comprare un libro")
else :
   print("no te comprare nada")

print(f"Te ganaste un regalo como premio.")

