#Variables

my_variable = "My String variable"
print(my_variable)

my_int = 5
print(my_int)

my_boolean = True
print(my_boolean)

my_int_to_str_variable = str(my_int)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


#Concatenacion de variables en un print
print("Hello","World",my_boolean,my_variable)

print("Este es el valor de:",my_boolean)

#Algunas funciones del sistema

print(len(my_variable))

#Variables en una sola linea
#Es una posibilidad pero no es una buena practica.
name, surname, alias, age = "Owen", "Rojas", "Zark", 22
print("Me llamo:", name, surname, "Tengo:", age,"años", "Mi alias es: ", alias)


#Input es para teclear datos
first_name = input("Cual es tu nombre?")


#Forzamos el tipo de variable ""
address: str = "Mi direccion"

address = 32

print(address)
print(type(address))