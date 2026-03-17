#Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [22, 34, 23, 45, 31, 31, 15]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.83, "Owen", "Rojas"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list[3])
print(my_list.count(31))#Devuelve las veces que se repite un valor


edad, peso, nombre, apellido = my_other_list

print(edad)

print(my_list + my_other_list)

my_list_suma = [my_list + my_other_list]

print(my_list_suma)


my_other_list.append("OwenZRK") #Agrega un valor a la lista al final
print(my_other_list)

my_other_list.insert(1, "Rojo")#Agrega un valor a la casilla indicada
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")#Borra un valor especificado (el primero que encuentra)
print(my_other_list)

my_list.remove(31)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element =my_list.pop(2)

print(my_pop_element)
print(my_list)

del my_list[2]#Elimina por indice
print(my_list)

my_new_list = my_list.copy() #Copia hasta este punto el contenido de la lista

my_list.clear()#Borra toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))