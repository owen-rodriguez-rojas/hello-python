#Excepciones - Exceptioon Handling


num1 = 5
num2 = 1

num2 = "5"

#try except
try:
    print(num1 + num2)
    print("No se a producido un error")
except:
    #Se ejecuta si se produce una excepcion
    print("Se a producido un error")
    
    
#try except else finally
try:
    print(num1 + num2)
    print("No se a producido un error")
except:
    print("Se a producido un error")
else: #Opcional
    #Se ejecuta si no se produce una excepcion
    print("La ejecución continua correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continua")
    
#Excepciones por tipo

try:
    print(num1 + num2)
    print("No se a producido un error")
except ValueError:
    #Se ejecuta si se produce una excepcion
    print("Se a producido un ValueError")
except TypeError:
    #Se ejecuta si se produce una excepcion
    print("Se a producido un TypeError")


#Captura de la informacion de la excepcion

try:
    print(num1 + num2)
    print("No se a producido un error")
except ValueError as error:
    print(error)
except Exception as e:
    print(e)

