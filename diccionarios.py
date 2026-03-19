#Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Owen", "Apellido":"Rojas", "Edad":22, 1:"Pyhton"}

my_dict = {
    "Nombre":"Owen", 
    "Apellido":"Rojas", 
    "Edad":22, 
    "Lenguajes":{"Pyhton","Java","CSS"},
    1:1.83
    }
print(my_other_dict)
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Misael"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Insurgentes"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Owen" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dic = dict.fromkeys((my_list))
print(my_new_dic)


my_new_dic = dict.fromkeys((my_dict))  #Se crea un nuevo diccionario para reutilizar las claves
print(my_new_dic)

my_new_dic = dict.fromkeys(my_dict, ["Owen"])
print(my_new_dic)

print(list(my_new_dic.values()))
print(tuple(my_new_dic))
print(set(my_new_dic))
