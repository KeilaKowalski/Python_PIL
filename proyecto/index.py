def menu():
    stock = iniciarVec()
    # print((stock))
    print("Miembros: \n Basualdo, Franco Emannuel \n Ibars, Yaco \n Ruiz, Matias \n Kowalski, Keila")
    input("\n Presione enter para seguir..")

    while True:
        print("\n \n BIENVENIDO AL MENU CONTROL DE STOCK DE LA EMPRESA PIL: \n \n")
        print("Lista de opciones disponibles")
        print("1) Mostrar todos los productos disponibles")
        print("2) Mostrar producto por categoria")
        print("3) Realizar compra de stock")
        print("4) Realizar venta de stock")
        print("5) Salir del menu \n")
        opcion = input("Ingrese la opcion de que desea consultar: ")
        if opcion == "1":
            mostrarTodo(stock)
        elif opcion == "2":
            mostrarUnaCate(stock)
        elif opcion == "3":
            ingreso_stock(stock)
        elif opcion == "4":
            ventaProductos(stock)
        elif opcion == "5":
            break
        else:
            print("La opcion marcada no esta entre las opciones del menu")


def iniciarVec():
    vector = []
    prod = {
        "cate": "Camperas",
        "name": "Campera Negra",
        "cantidad": 15,
        "precio": 500
    }
    prod1 = {
        "cate": "Camperas",
        "name": "Campera Roja",
        "cantidad": 15,
        "precio": 500
    }
    prod2 = {
        "cate": "Camperas",
        "name": "Campera Azul",
        "cantidad": 15,
        "precio": 500
    }
    prod3 = {
        "cate": "Sweters",
        "name": "Sweters Negro",
        "cantidad": 15,
        "precio": 500
    }
    prod4 = {
        "cate": "Accesorios",
        "name": "Reloj",
        "cantidad": 15,
        "precio": 500
    }
    prod5 = {
        "cate": "Remeras",
        "name": "Remera Adidas",
        "cantidad": 15,
        "precio": 500
    }
    prod6 = {
        "cate": "Remeras",
        "name": "Remera Nike",
        "cantidad": 15,
        "precio": 500
    }
    prod7 = {
        "cate": "Pantalones",
        "name": "Pantalon Verde",
        "cantidad": 15,
        "precio": 500
    }
    prod8 = {
        "cate": "Camperas",
        "name": "Campera Bordo",
        "cantidad": 15,
        "precio": 500
    }
    #Camperas
    vector.append(prod8)
    vector.append(prod)
    vector.append(prod1)
    vector.append(prod2)
    #Pantalones
    vector.append(prod7)
    #Remeras
    vector.append(prod6)
    vector.append(prod5)
    #Accesorios
    vector.append(prod4)
    #Swetters
    vector.append(prod3)
    return (vector)


def mostrarTodo(vector):
    for v in range(len(vector)):
                print(" \n Categoria: {} \n Nombre: {} \n Cantidad: {} \n Precio {}".format(vector[v].get("cate"), vector[v].get("name"), str(vector[v].get("cantidad")), str(vector[v].get("precio"))))
    input("Aprete enter para seguir...")

def mostrarUnaCate(vector):
    vectorCate = ["Camperas", "Sweters", "Accesorios", "Remeras", "Pantalones"]
    print("Que categoria quieres ver:")
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones")
    categoria = int(input("\n Ingrese la opcion que desea ver: "))
    print("")
    print("La categoria que elegiste es: " + vectorCate[categoria - 1])
    for v in range(len(vector)):
        if(vectorCate[categoria - 1] == vector[v].get("cate")):
                print("\n Nombre: {} \n Cantidad: {} \n Precio {}".format(vector[v].get("name"), str(vector[v].get("cantidad")), str(vector[v].get("precio"))))


def ingreso_stock(vector):
    """summary: Brinda un menú de opciones con categorías de ropa,
    para que se pueda ingresar en la categoría adecuada el nuevo stock para la tienda.

    Args:
        Recibe un vector con todos los productos.
    Returns:
        print: stock completo, con el producto nuevo ingresado.
    """
    vectorCate = ["Camperas", "Sweters", "Accesorios", "Remeras", "Pantalones"]
    print('\n \nIngreso de Stock\n')
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones\n")

    categoria = int(input('Seleccione una Categoría:\t'))

    nombre = input('Ingresar nombre del producto:\t')
    cantidad = int(input('Ingresar cantidad de productos:\t'))
    precio = int(input('Ingresar costo:\t'))

    posicion = buscar(vector, categoria, nombre)

    if(posicion == -1):
        prod = {
        "cate": vectorCate[categoria - 1],
        "name": nombre,
        "cantidad": cantidad,
        "precio": precio
    }
        vector.append(prod)
    else:
        nueCant = vector[posicion].get("cantidad") + cantidad
        vector[posicion].update({"cantidad" : nueCant })
        vector[posicion].update({"precio" : precio})
    print(" \n Categoria: {} \n Nombre: {} \n Cantidad: {} \n Precio {}".format(vector[posicion].get("cate"), vector[posicion].get("name"), str(vector[posicion].get("cantidad")), str(vector[posicion].get("precio"))))


def buscar (vector,categoria, nombre):
    for v in range(len(vector)):
        if nombre.upper() == str(vector[v].get("name")).upper(): #and categoria == vector[v].get("cate") :
                print(v)
                return v
    print("LPM")
    return -1


def ventaProductos(stock):
    mostrarTodo(stock)

    print('\n \nVenta de Stock\n')
    print("1) Camperas")
    print("2) Sweters")
    print("3) Accesorios")
    print("4) Remeras")
    print("5) Pantalones\n")

    categoria = int(input('Seleccione una Categoría:\t'))
    if (categoria > 5 or categoria < 1):
        print("Excede del rango de las opciones")
    else:
        nombre = input("Ingrese el nombre del producto que desea buscar: ")
        cantidadProd = int(input("Ingrese la cantidad del producto que desea: "))
        posicion = buscar(stock, categoria -1, nombre )
        if posicion == -1:
            print("No se encontro el producto")
        else:
            if stock[posicion].get("cantidad") >= cantidadProd:
                nuevaCant = (stock[posicion].get("cantidad") - cantidadProd)
                stock[posicion].update({"cantidad": nuevaCant})
                print("Muchas gracias por su compra!")
                print("Lo que usted tiene que abonar es $" + str(stock[posicion].get("precio") * cantidadProd))

            else:
                print("No tenemos la cantidad solicitada {}, tenemos {}".format(cantidadProd, stock[posicion].get("cantidad")))
                decision = input("Desea realizar la compra del stock total: S/N")
                if decision == "S" or decision == "s":
                    print("\nMuchas gracias por la compra")
                    print("Lo que usted tiene que abonar es ${} \nVuelva pronto".format(stock[posicion].get("precio") * stock[posicion].get("precio")))
                    stock[posicion].update({"cantidad": 0})
        input("Aprete enter para seguir...")

# Lamado a ejecutar la función de menú principal.
menu()
