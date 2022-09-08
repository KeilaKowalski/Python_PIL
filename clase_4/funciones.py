# Funcion base
def sumar(a, b):
    resultado = a + b 
    return resultado

print(sumar(2,3))

# Funcion 2
def resta():
    resultado = 2 - 3
    return resultado

print(resta())

# Funcion 3
def saludo(cantidad_saludos):
    """Esta funcion recoge los nombres ingresado por el usuario y devuelve los mismos en formato lista."""
    
    lista_nombres = []
    
    # Bucle de ingreso de nombres
    for i in range(cantidad_saludos):
        nombre = input("Ingrese su nombre: ")
        print("Hola " + nombre)
        lista_nombres.append(nombre)

    print(lista_nombres)
    return lista_nombres


def orden(lista, sentido):
    """Esta funcion nos permite ordenar listas en base a un sentido determinado."""
    lista.sort(reverse = sentido)
    return lista

nombres = saludo(int(input("Ingrese la cantidad de saludos a efectuar: ")))
print(
    orden(nombres, False)
)



