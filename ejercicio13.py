n = int(input("Introduce un número: "))
# n indica el número introducido
if n < 1:
    print("Debe ser mayor que 0")
else:
    for i in range(1, n + 1): # en python puedes meter el contador dentro del rango
        print(f"Número: {i}")
