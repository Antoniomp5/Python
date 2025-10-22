#Función contar vocales y sustituirlas

def cambio(frase):
    vocales = "aeiouAEIOU"
    contador = 0

    for v in vocales:
        contador += frase.count(v)

    for v in vocales:
        frase = frase.replace(v, "x")
        
    print(f"Cantidad de vocales: {contador}")
    return frase


print(cambio(input("Introduce la oración: ")))
