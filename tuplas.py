#Tuplas

"""
La diferencia de una tupla a una lista, es que son valores
inmutables, podemos guardar datos en ellas, pero ya tenemos
valores inicializados

"""


my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.82, "Owen", "Rojas")
my_other_tuple = (32, 45, 44, 21)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[-1])
print(my_tuple[0])

print(my_tuple.count("Rojas"))

print(my_tuple.index("Owen")) #Muestra el numero de indice
print(my_tuple.index("Rojas"))

#my_tuple[1] = 1.90 ERROR

my_suma_tuple = my_tuple + my_other_tuple
print(my_suma_tuple)

print(my_suma_tuple[3:6])


my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Rodriguez"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
#print(my_tuple) name 'my_tuple' is not defined