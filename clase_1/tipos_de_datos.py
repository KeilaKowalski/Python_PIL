# Str
cadena = "esto es una cadena"
print(cadena[0:4])
print(cadena[-1])

# Metodos
print(cadena.upper())
print(cadena.split())

# List
lista_1 = ["hola", 4, 2.5, True, [1,2], ("a", "b")]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_uno = lista_1[3]
print(var_uno)
print(type(var_uno))

# Metodos
lista_1.append("lista")
print(lista_1)

print(lista_1.index(("a", "b")))

lista_1.insert(1, False)
print(lista_1)

# Diccionario
usuario = {
    "nombre": "Octavio",
    "apellido": "Gomez",
    "edad": 38,
    "hobbies": ["Futbol", "Musica"],
    "mascotas": False,
}
print(usuario)
print(usuario["edad"])
print(len(usuario))

# Metodos
print(usuario.get("puesto", "no encontrado"))

keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))

print(usuario.values())
values_usuario = list(usuario.values())
print(usuario.get(values_usuario[2]))


