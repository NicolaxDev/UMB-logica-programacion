"""
7. La hora laboral tiene un coste de $8.95. Calcular el valor de la jornada segun la cantidad de horas trabajadas, teniendo en cuenta que la jornada diaria normal es de 8 horas. si se exceden las horas se cuentan como extras y tienen un recargo del 25%. La jornada maxima de trabajo es de 12 horas
"""
horas = float(input("Ingrese las horas trabajadas >> "))
valorHora = 8.95

if(horas > 0 and horas <= 12):
    if(horas > 8):
        valorJornada = (8 * valorHora) + (((horas - 8)*valorHora)*0.25)
    else:
        valorJornada = horas*valorHora
else:
    print("Jornada ingresada invalida")

print(valorJornada)