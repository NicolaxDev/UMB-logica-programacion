"""
10. Escribe un programa que lea del teclado un carácter e indique en la pantalla si el carácter es una vocal minúscula o no.
"""
caracter = input("Ingrese un caracter >> ")
if(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
    print("El caracter: ", caracter, " es una vocal y es minuscula")
elif(caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U"):
    print("El caracter: ", caracter, "es una vocal y es mayuscula")
else:
    print("El caracter: ", caracter, "NO ES UNA VOCAL")