"""
1. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no. teniendo en cuenta que la mayoria de edad comienza a los 18 años.
"""

edad = int(input("Ingrese su edad: "))

if (edad >= 18):
    print("Usted es mayor de edad: ", edad)
elif(edad < 0):
    print("Error, edad no valida")
else:
    print("Usted no es mayor de edad: ", edad)