class ventas():
    def Calcularcomisiones(self):
        SB, venta1, venta2, venta3, Total_ventas=0,0,0,0,0
        comision, sueldo_total = 0,0
        SB=float(input("ingrese el sueldo base: "))
        venta1=float(input("ingrese el valor de las 1 ventas:"))
        venta2=float(input("ingrese el valor de las 2 ventas:"))
        venta3=float(input("ingrese el valor de las 3 ventas:"))
        Total_ventas=venta1+venta2+venta3
        comision = Total_ventas*0.10
        sueldo_total = SB+comision
        print("sueldo base es: $",SB)
        print("Total de ventas: $",Total_ventas)
        print("comision de las ventas: $",comision)
        print("El sueldo total es: $",sueldo_total)
venta=ventas()
venta.Calcularcomisiones()