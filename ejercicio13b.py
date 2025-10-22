n = int(input("Introduce un número: "))
# n indica el número introducido
if n < 1:
    print("Debe ser mayor que 0")
else:
    c = 1 # c es el contador
    while c <= n:
        print(f"Número: {c}")
        c += 1
