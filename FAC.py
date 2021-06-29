class DEBER:
    def _init_(self):
        pass
    def Factorial(self):
        N=int(input("ingrese la cantidad de numeros: "))
        for i in range(N):
            numero=int(input("ingrese numero: "))
            acu=1
            for num in range(numero,1,-1):
                acu=acu*num
            print("numero= {} factorial={}".format(numero,acu))

DEBER=DEBER()
DEBER.Factorial()