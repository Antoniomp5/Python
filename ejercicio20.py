numero = int(input("Introduce el número: "))
factorial = 1
for i in range(1, numero + 1):
    factorial = factorial * i
print(f"El resultado de {numero}! = {factorial}")
