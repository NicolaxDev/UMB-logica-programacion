n = int(input("Ingrese el numero >> "))

a = 0
b = 1

print(a)
print(b)

suma = 1
for i in range (1, n-1):
    fibo = a + b
    print(fibo)
    a = b
    b = fibo
    suma += fibo

print("La suma es: ", suma)