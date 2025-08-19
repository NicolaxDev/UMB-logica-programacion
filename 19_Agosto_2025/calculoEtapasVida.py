edad = int(input("Ingrese la edad: "))

if (edad >= 0 and edad <= 6):
    print("Estas en etapa de INFANCIA")
elif (edad > 6 and edad <= 12):
    print("Estas en etapa de NIÑEZ")
elif (edad > 12 and edad <= 20):
    print("Estas en etapa de ADOLESCENCIA")
elif (edad > 20 and edad <= 25):
    print("Estas en etapa de JUVENTUD")
elif (edad > 25 and edad <= 60):
    print("Estas en etapa de ADULTEZ")
else:
    print("Estas en etapa de VEJEZ")