#Strings 

my_string = "My String"
my_other_string = 'Mi String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string escapado"
print(my_scape_string)


#Formateo

name, surname, age = "Owen", "Rojas", 22

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
language = "python"

a, b, c, d, e, f = language

print(a)
print(e)

#Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[0:2]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize()) #Pone la primera en mayus
print(language.upper()) #Pone todas em mayusculas
print(language.count("t")) #Cuenta cuantas letras tiene en especifico
print("1".isnumeric()) #Te dice si es numero o no
print(language.isnumeric())
print(language.lower())#Convierte a todas em minusculas
print(language.upper().isupper()) 
print(language.startswith("py"))