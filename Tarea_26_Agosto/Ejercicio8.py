"""
8. Crea un programa en el que el usuario ingrese dos numeros, se deve devolver la diferencia de el mayor entre el menor.
"""

n1 = float(input("Ingrese el primer numero >> "))
n2 = float(input("Ingrese el segundo numero >> "))

if(n1>n2):
    print("El resultado de ", n1, "-", n2, "es: ", (n1 - n2))
elif(n1<n2 or n1==n2):
    print("El resultado de ", n2, "-", n1, "es: ", (n2 - n1))