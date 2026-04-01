#Bucles/Loops/Ciclos

#While
#><

my_condition = 0


while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: #Opcional
    print("Mi condicion es mayor o igual que 10")


print(". . . . . . . . . . .")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
        
    print(my_condition)
    
print(". . . . . . . . . . .")

#For
#><

my_list = [22, 34, 23, 45, 31, 31, 15]

for element in my_list:
    print(element)
    
    
    
    
my_tuple = (22, 1.82, "Owen", "Rojas")
for element in my_tuple:
    print(element)    
    
my_set = {"Owen", "Rojas", 22}
for element in my_set:
    print(element)
    
my_dict = {"Nombre":"Owen", "Apellido":"Rojas", "Edad":22, 1:"Pyhton"}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para mi dic a finalizado")
    
print(". . . . . . . . . . .")
    
for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi dic a finalizado")