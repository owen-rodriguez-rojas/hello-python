#Manejo de paquetes en Python

#PIP 

import numpy

numpy_array = numpy.array([35, 45, 55, 23, 67, 89, 90])

print(type(numpy_array))

print(numpy_array*2)

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

#Paquetes Aritmeticos
from mypackage import arithmetics

print(arithmetics.suma(5, 10))

