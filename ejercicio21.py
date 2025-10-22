# Función par o impar
def par_o_impar(num):
    if num % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")

# Programa principal        
num = int(input("Introduce el número: "))
par_o_impar(num)
