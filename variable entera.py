class sueldo():
    def sueldo_Aumento(self):
        S = float(input("Ingrese Sueldo: "))
        if S > 600:
            A = S * 0.10
            S = S + aum
            print(" aumento", S)
        else:
            print("No aumento")
            print("El sueldo es: ", S)


sueldo = sueldo()
sueldo.sueldo_Aumento()
