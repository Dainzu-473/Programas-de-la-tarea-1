edad = int(input("Ingresa una edad"))

if edad < 12:
    costo = 50
elif 12 <= edad <= 17:
    costo = 80
else:
    costo = 120

print(f"El costo de la entrada es: {costo}")