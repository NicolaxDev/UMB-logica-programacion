horas = float(input("Ingrese las horas de estacionamiento: "))
if(horas <= 2 and horas > 0):
    print("Su tarifa de estacionamiento es: 0, estancia en horas: ", horas)
elif(horas > 2 and horas <= 5):
    estancia = horas - 2
    tarifa = estancia * 5
    print("Su tarifa de estacionamiento es: ", tarifa, ", estancia en horas: ", horas)
elif(horas > 5):
    estancia = horas - 5
    valorHora3 = 15
    tarifa = (estancia * 10) + valorHora3
    print("Su tarifa de estacionamiento es: ", tarifa, ", estancia en horas: ", horas)
else:
    print("Error, las horas son invalidas")