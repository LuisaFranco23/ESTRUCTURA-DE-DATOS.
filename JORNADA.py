class DEBER:
    def __init__(self):
        pass

    def CalcularJornada(self):
        HORAST, HORASEX, HORASET = 0, 0, 0
        ph, phe, pt, ph8 = 0, 0, 0, 0
        ht = int(input("Ingrese horas trabajadas : "))
        ph = float(input("ingrese valor hora : "))
        if HORAST > 40:
            HORASEX = HORAST - 40
            if HORASEX > 8:
                HORASET = HORASEX - 8
                ph8 = 8 * ph * 2
                phe = HORASET * ph * 3
            else:
                phe = 0
                ph8 = HORASEX * ph * 2
            pt = 40 * ph + ph8 + phe
        else:
            pt = HORAST * ph
        print("sobretiempo<8: {} Sobretiempo>8: {} jornada : {} ".format(ph8, phe, pt))


tarea = DEBER()
tarea.CalcularJornada()
