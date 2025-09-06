l1 = float(input("Ingrese la longitud del lado 1: "))
l2 = float(input("Ingrese la longitud del lado 2: "))
l3 = float(input("Ingrese la longitud del lado 3: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):

    if l1 == l2 == l3:
        print("El triangulo es equilatrero. ")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("El triangulo es isoceles. ")
    else:
        print("El triangulo es escaleno. ")
else:
    print("Los valores ingresados no forman un triangulo. ")    