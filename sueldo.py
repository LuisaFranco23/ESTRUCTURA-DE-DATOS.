class sueldo():
    def sueldo_Aumento(self):
        S = float(input("Ingrese Sueldo: "))
        if S > 600:
            A = S * 0.10
            A = S + A
            print("Obtiene aumento", S)
        else:
            print("No obtiene aumento")
            print("El sueldo es: ", S)


sueldo = sueldo()
sueldo.sueldo_Aumento()
