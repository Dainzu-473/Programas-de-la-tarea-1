calificacion = int(input("Ingrese una calificacion (0-100): "))

if 90 <= calificacion <= 100:
    letra = "A"
elif 80 <= calificacion <= 89:
    letra = "B"
elif 70 <= calificacion <= 79:
    letra = "C"
elif 60 <= calificacion <= 69:
    letra = "D"
elif 0 <= calificacion <= 60:
    letra = "F"
else:
    letra = None

if letra:
    print(f"La calificacion {calificacion} es igual a la letra '{letra}'. ")
else:
    print("Calificacion no valida. Debe de ser entre 0 y 100. ")    