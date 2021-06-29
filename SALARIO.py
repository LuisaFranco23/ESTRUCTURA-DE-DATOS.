class DEBER:
    def __init__(self):
        pass
    def Calcular(self):
        print("_______________________________________")
        SB=float(input("Ingrese Salario Base:"))
        V1=float(input("Ingrese valor de venta 1:"))
        V2=float(input("Ingrese valor de venta 2:"))
        V3=float(input("Ingrese valor de venta 3:"))
        TV=V1+V2+V3
        C=TV*0.1
        TR=SB+C
        print()
        print("Su Total a Recibir es: ")
        print("$",TR)
        print("_______________________________________")
        input("enter para salir")
tarea= DEBER()
tarea.Calcular()