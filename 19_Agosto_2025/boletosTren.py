precioBoletoBase = 200
esMayor = False
esEstudiante = False

cambiarEstado = int(input("Si el usuario es estudiante ingrese 1. \nSi el usuario es adulto mayor ingrese 2. \nSi tiene ambas tarjetas ingrese 3. \nSi no aplica ingrese 0: \n\n>>>> "))
#Establecer valores segun lo que ingresa el cliente
if (cambiarEstado == 1):
    esEstudiante = True
    print("Aplica descuento estudiante")
elif (cambiarEstado == 2):
    esMayor = True
    print("Aplica descuento adulto mayor")
elif (cambiarEstado == 3):
    esMayor = True
    esEstudiante = True
    print("Aplica descuento mayor")
else:
    print("No cuenta con descuentos")

#Calcular el valor del ticket
if (esMayor == True or (esMayor == True and esEstudiante == True)):
    print("El precio final del boleto es: ", 100)
elif (esEstudiante == True):
    print("El precio final del boleto es: ", 150)
else:
    print("El precio final del boleto es: ", 200)