"""
4. Escriba un programa que pida el número de mes (del 1 al 12) y el año e imprima el número de días que tiene el mes.
"""
mes = int(input("Ingrese el numero del mes a consultar >> "))

if(mes >= 1 and mes <= 12):
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        print("El mes tiene 31 dias")
    elif(mes==4 or mes==6 or mes==9 or mes==11):
        print("El mes tiene 30 dias")
    else:
        print("El mes tiene 28 o 29 días (si es año bisiesto)")
else:
    print("Mes ingresado invalido")