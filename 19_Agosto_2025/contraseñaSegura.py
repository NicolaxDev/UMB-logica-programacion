contraseña = input("Ingrese una contraeña >> ")
lowerC = False
upperC = False
charE = False
dig = False

print("ATRIBUTOS: \ncaracter especial, numero, mayuscula y minuscula")
print("\nTu contraseña sera excelente si cumple con todos los atributos\nTu contraseña sera buena si tiene por lo menos dos atributos\nTu contraseña sera debil si tiene por lo menos un atributo\nTu contraseña sera mala si no tiene ningun atributi\n\n")

caracteresEspeciales = ["@", "$", "%", "#", "/", "&", "="]
for c in caracteresEspeciales:
    if(contraseña.find(c) >= 0):
        charE = True

lowerCase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
upperCase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

for l in lowerCase:
    if(contraseña.find(l) >= 0):
        lowerC = True

for l in upperCase:
    if(contraseña.find(l) >= 0):
        upperC = True

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
for n in numeros:
    if(contraseña.find(n) >= 0):
        dig = True

if(upperC == True and lowerC == True and dig == True and charE == True):
    print("Tu contraseña es excelente")
elif(upperC == True or lowerC == True or dig == True or charE == True):
    print("Tu contraseña es debil")
elif(upperC == False and lowerC == False and dig == False and charE == False):
    print("Tu contraseña es mala")
else:
    print("Tu contraseña es buena")