"""
3. Cree un programa que dados 3 numeros enteros determine el numero intermedio.
"""
print("A continuacion ingrese 3 numeros enteros y que sean diferentes")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if((n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3)):
    print("El numero intermedio es: ", n1)
elif ((n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3)):
    print("El numero intermedio es: ", n2)
elif ((n3 > n1 and n3 < n2) or (n3 < n1 and n3 > n2)):
    print("El numero intermedio es: ", n3)
else:
    print("Numeros ingresados no validos")