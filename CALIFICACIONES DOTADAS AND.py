class calificaciones():
    def calificacionesD(self):
        print("Calificaciones Denotadas de C1 y C2")
        C1=float(input("Ingrese calificacion de C1: "))
        C2=float(input("Ingrese calificacion de C2: "))
        if C1>=70:
            print("Aprobado C1",C1)
        else:
            print("Rechazado C1",C1)
            if C2>=70:
                print("Aprobado C2",C2)
            else:
                print("Rechazado C2",C2)
calificación=calificaciones()
calificación.calificacionesD()