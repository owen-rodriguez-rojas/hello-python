#Manejo de ficheros

import os

#.txt file

txt_file = open("my_file.txt", "w+") # Leer y escribir

txt_file.write("Mi nombre es Owen Misael\nMi apellido es Rodriguez\nTengo 22 Años\nMi lenguaje favorito es Python\nY mi proximo lenguaje a aprender es Javascript")
#print(txt_file.read())
print(txt_file.read(10))

print(txt_file.readline())
print(txt_file.readline())

for i in txt_file.readlines():
    print(i)
    

txt_file.write("\nY mi proximo lenguaje a aprender es Javascript")
print(txt_file.readline())

txt_file.close()

#os.remove("my_file.txt")


#.json file

import json

json.dump

json_file = open("my_file.json", "w+")

json_test = {
    "Nombre":"Owen",
    "Edad": 22,
    "Lenguajes":["Python","Java","JavaScript"],
    "GitHub": "https://github.com/owen-rodriguez-rojas"
}

json.dump(json_test, json_file, indent=4)

json_file.close()

    
with open("my_file.json") as my_other_file:
    for i in my_other_file.readlines():
        print(i)



json_dict = json.load(open("my_file.json"))
print(json_dict)
print(type(json_dict))

print(json_dict["Nombre"])

#.csv file

import csv

csv_file = open("my_file.csv", "w+")

csv_write = csv.writer(csv_file)

csv_write.writerow(["Nombre", "Edad", "Lenguaje", "GitHub"])
csv_write.writerow(["Owen", "22", "Python", "https://github.com/owen-rodriguez-rojas"])
csv_write.writerow(["Misael", "", "English", ""])

csv_file.close()

with open("my_file.csv") as my_other_file:
    for i in my_other_file.readlines():
        print(i)
        
        
#.xlsx file
#import xlrd Debe instalarse 


#.xml file

import xml