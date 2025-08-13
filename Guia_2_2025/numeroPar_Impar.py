numero = int(input("Ingrese un numero entero: "))

if(numero == 0):
    print("No es posible determinar el cero")
else:
    mod = numero % 2
    if(mod == 0):
        print("El numero: ", numero, "es par")
    else:
        print("El numero: ", numero, "es impar")