nVentas = int(input("Ingrese el numero de ventas que desea registrar >> "))
catTecnologia = 0
catRopa = 0
catHogar = 0
totalVendido = 0
ventaMasGrande = 0
for i in range(1, nVentas+1):
    print("----------Venta", i, "----------")
    valorVenta = float(input("Ingrese el valor de la venta >> "))
    totalVendido += valorVenta
    if valorVenta > ventaMasGrande:
        ventaMasGrande = valorVenta
    categoria = int(input("Seleccione la categoria correspondiente\n1. Tecnologia\n2. Ropa\n3. Hogar\n >> "))
    print("Venta registrada con exito!!")
    if categoria == 1:
        catTecnologia += 1
    elif categoria == 2:
        catRopa += 1
    elif categoria == 3:
        catHogar += 1
    else:
        print("Categoria erronea")

print("-------------------------")
print("Resumen del dia ")
print("Se realizaron: ", nVentas, "ventas en el dia")
print("Se obtuvieron ingresos de: ", totalVendido)
print("La venta mas grande fue de: ", ventaMasGrande)
print("Las ventas por categoria:\n1. Tecnologia", catTecnologia, "\n2. Ropa", catRopa, "\n3. Hogar", catHogar)