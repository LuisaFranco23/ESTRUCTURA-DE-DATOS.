def vocales(frase):
    for car in frase:
        if car in ('a', 'e', 'i', 'o', 'u'):
            print(car)


Oracion = input('Ingrese una Oracion: ')
vocales(Oracion.lower())


def Promedio(Notas):
    Summ = 0
    for n in Notas:
        Summ += n
    return Summ / len(Notas)


# llamada a funcion
listanotas = [3, 6, 9, 12, 15]
Prom = Promedio(listanotas)
print('Promedio: {} = {}'.format(listanotas, Prom))
