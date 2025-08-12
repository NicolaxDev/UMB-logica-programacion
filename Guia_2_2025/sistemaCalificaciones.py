calificacion = float(input("Ingresa la calificacin obtenida: "))

if(calificacion < 0 or calificacion > 100):
    print("La calificacion que ingresaste no es valida: ", calificacion)
elif(calificacion >= 60):
    print("Haz aprobado!!!, con: ", calificacion, "sobre: 100")
else:
    print("Haz reprobado :(, necesitas minimo 60 y obtuviste: ", calificacion)