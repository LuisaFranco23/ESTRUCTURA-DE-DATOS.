class descuento():
    def cantidaddescuento(self):
     TTc= float(input("Ingrese el valor del total de compra : "))
     DES= TTc*0.15
     Cp= TTc-DES
     print("El descuento de la compra es : ",DES)
     print("La cantidad a pagar es: $ ",Cp)
descuento=descuento()
descuento.cantidaddescuento()