class sumaproducto():
    def __init__(self):
        pass

    def cen(self):
        Prod = 1
        S = 0
        num = int(input("Dijite un numero entero que no sea negativo: "))
        while num != -1:
            num = int(input("Ingrese un numero: "))
            S = S + num
            Prod = Prod * num
        print("""Total de la suma es:""", S,
              """Total del producto es: """, Prod)


suma = sumaproducto()
suma.cen()