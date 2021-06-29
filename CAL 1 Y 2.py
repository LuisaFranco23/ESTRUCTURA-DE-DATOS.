class calificaciones():
    def calificacionesdotadas(self):
        print("Calificaciones Denotadas de C1 y C2")
        CAL1=float(input("Ingrese calificacion de C1: "))
        CAL2=float(input("Ingrese calificacion de C2: "))
        if CAL1>=80:
            print("Aprobado C1",CAL1)
        else:
            print("Rechazado C1",CAL1)
            if CAL2>=80:
                print("Aprobado C2",CAL2)
            else:
                print("Rechazado C2",CAL2)
calificación=calificaciones1()
calificación.calificacionesdotadas()