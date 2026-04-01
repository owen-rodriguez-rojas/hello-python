#Sets

"""
Un set no es una estructura ordenada
No se puede acceder a un elemento en concreto por que el
ordenamiento es aleatorio

"""

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Owen", "Rojas", 22}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("OwenZrk")
print(my_other_set)

my_other_set.add("OwenZrk") #Un set no admite repetidos
print(my_other_set)

print("Owen" in my_other_set)
print("Owem" in my_other_set)

my_other_set.remove("Rojas")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

#del my_other_set borra todo el objeto no lo limpia como el clear

