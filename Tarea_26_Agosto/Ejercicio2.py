"""
2. Calcule el interés mensual generado por un capital. La tasa de interés mensual depende del capital que fue depositado. Si el capital es menor de 500, la tasa de interés será del 2% mensual. Si el capital es mayor o igual que 500 pero menor o igual a 1500 entonces la tasa de interés es de 4.5%. Si el capital es mayor que 1500 la tasa de interés es del 9%. Se debe ingresar el capital y reportar el interés a un mes.
"""

capital = float(input("Ingrese el valor del capital >> "))

if(capital < 500):
    tasaInteres = 2
elif(capital >= 500 and capital <= 1500):
    tasaInteres = 4.5
elif(capital > 1500):
    tasaInteres = 9
else:
    print("Capital invalido")

interesMes = capital * (tasaInteres / 100)
print("Su capital: ", capital, "tiene un interes mensual del: ", tasaInteres, "% , a un mes su interes sera: ", interesMes)