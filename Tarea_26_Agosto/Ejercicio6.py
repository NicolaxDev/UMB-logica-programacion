"""
6. Calcule el valor de la funcion Fx dada por: x^3 + x/2, para x < 0 y 4x^2 – 2, para x ≥ 0.
"""
x = float(input("Ingrese el valor de X >> "))

if(x < 0):
    resultado = (x^3) + (x/2)
elif(x >= 0):
    resultado = (4*x^2) - 2

print("El valor de Fx es: ", resultado)