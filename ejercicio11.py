l1 = float(input("Lado uno: "))
l2 = float(input("Lado dos: "))
l3 = float(input("Lado tres: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
        print("El triángulo es equilátero")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("No es un triángulo válido")
