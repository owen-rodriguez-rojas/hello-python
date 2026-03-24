#Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"): #Esto es un constructor no una funcion
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} Esta caminando")
        
my_person = Person("Owen", "Rojas")
print(my_person.full_name)

my_person.walk()

my_other_person = Person("Misael", "Rodriguez", "Zark")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Tom Holland (Spiderman)"
print(my_other_person.full_name)