class numero():

    def Ncuadrados(self):
        N,S=0,0
        N=int(input("ingrese el limite de cuadrado:"))
        print("---------------")
        for i in range(1,N+1):
            print(i,"^2")
            print("+")
            S = S+(i**2)
            print("La suma de los cuadrados es: ",S)
numero=numero()
numero.Ncuadrados()  