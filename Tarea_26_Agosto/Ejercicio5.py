"""
5. Un estudiante recibe una propina mensual de $100. A fin de mes el estudiante rinde 3 exámenes (Informática, cálculo, Física). El papa ha decidido incentivarlo dándole una propina adicional de $20 por cada examen aprobado. Hacer un programa que determine cuanto de propina recibe el estudiante después de dar los exámenes.
"""
examenesAprobados = int(input("Ingrese cuantos examenes de 3 aprobo >> "))
propinaBase = 100
propinaExamen = 20

calculoPropina = propinaBase + (propinaExamen * examenesAprobados)

if(examenesAprobados == 1):
    print("La propia que recibe es de: ", calculoPropina)
elif(examenesAprobados == 2):
    print("La propia que recibe es de: ", calculoPropina)
elif(examenesAprobados == 3):
    print("La propia que recibe es de: ", calculoPropina)
elif(examenesAprobados > 3):
    print("Cantidad de examenes invalida")
else: 
    print("La propia que recibe es de: ", calculoPropina)