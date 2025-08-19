codigo = int(input("Ingrese el codigo >> "))

esPar = False
if((codigo % 2) == 0):
    esPar = True

if(esPar == True and (codigo >= 100 and codigo <=200)):
    print("EXITO")
elif((codigo % 7) == 0 and (codigo % 3) == 1):
    print("ATENCION")
elif(esPar == False and codigo != (codigo >= 250 and codigo <= 300)):
    print("ERROR")
else:
    print("DESCONOCIDO")

