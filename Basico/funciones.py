#Funciones

def my_func ():
    print("Esto es una funcion")
    
    
my_func()


def sum_two_values(first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 6)
sum_two_values(7, 100)
sum_two_values("7", "100")
sum_two_values(5.2, 6.4 )



def sum_two_values_with_return(first_number, second_number):
    my_sum = first_number + second_number
    return my_sum


my_result = sum_two_values_with_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(name="Owen", surname="Rojas")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
    
print_name_with_default("Owen", "Rojas", "Zark")
print_name_with_default("Owen", "Rojas")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_upper_texts("Hola", "Python", "Owen")