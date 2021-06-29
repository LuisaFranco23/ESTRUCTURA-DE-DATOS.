class primo():

    def Nprimo(self):
        print("NÚMERO PRIMO")
        pri = 0
        div = 2
        num = int(input("ingrese un numero entero : "))
        while div < num and pri == 0:
            Res = num % div
            print(Res)
            if Res == 0:
                pri += 1
            div += 1
        if pri == 0:
            print("El numero", num, "es primo")
        else:
            print("El numero", num, "no es primo")


numero = primo()
numero.Nprimo()