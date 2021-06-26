class ciclo:

    def __init__(self,num=20):
        self.numero=num


    def usowhile (self):
        print("dentro de la clase",self.numero)
        LETRA=""
        while LETRA not in ("p","q","r","s","t"):
            LETRA =input("ingrese letra: ").lower()
            #caracter= caracter.lower()

        print("si es la letra correcta:{} si es letra".format(LETRA))

ciclo1= ciclo()
print("fuera de la clase",ciclo1.numero)
print(ciclo1.usowhile())





