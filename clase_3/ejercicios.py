# Ejercicio1
""" 
rta = 0
while rta != 4:
    print("\n1. Deposito")
    print("2. Extraccion")
    print("3. Transferencia")
    print("4. Salir \n")
    rta = int(input("Ingrese el numero de la operacion que desee: \n"))
    if(rta == 1):
        print(">Usted eligio deposito \n")
    elif(rta == 2):
        print(">Usted eligio extraccion \n")
    elif(rta == 3):
        print(">Usted eligio transferencia \n")
print("\nHa salido del programa. Hasta luego!")
"""

# Ejercicio2
num1 = int(input("\ningrese un numero entero: "))
num2 = int(input("ingrese otro numero entero: "))
for i in range(num1, num2, 2):
    print(i)