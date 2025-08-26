"""
9. En un tramo de un rally los conductores no deben ir ni demasiado rápido ni demasiado lentos. Este ejercicio debe tomar la longitud del tramo en kilómetros y el tiempo empleado, si la velocidad está entre 40 y 60 km/h el conductor pasa la prueba en caso contrario es descalificado.
"""
distancia = float(input("Ingrese la longitud del tramo en KM >> "))
tiempo = float(input("Ingrese el tiempo empleado en minutos >> "))

tiempoHoras = tiempo/60

velocidad = distancia/tiempoHoras

if(velocidad >= 40 and velocidad <= 60):
    print("Pasa la prueba con una velocidad de: ", velocidad, "km/h")
else:
    print("NO pasa la prueba, velocidad: ", velocidad, "km/h")