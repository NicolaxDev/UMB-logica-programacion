angulo = float(input("Ingrese el angulo >> "))

if(angulo == 90):
    print("Es un angulo RECTO")
elif(angulo > 90):
    print("Es un angulo OBTUSO")
elif(angulo < 90):
    print("Es un angulo AGUDO")
elif(angulo == 180):
    print("Es un angulo LLANO")
elif(angulo == 360):
    print("Es un angulo COMPLETO")
elif(angulo > 180):
    print("Es un angulo CONCAVO")
elif(angulo < 180):
    print("Es un angulo CONVEXO")