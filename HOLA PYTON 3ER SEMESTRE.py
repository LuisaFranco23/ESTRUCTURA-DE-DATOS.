import math
N1, N2, N, Men = 14.555,  10.3,  2,  '1234'
print(math.ceil(N1), '\t',math.floor(N1))
print(round(N1,1),'\t',type(N),'\t',type(Men))
# funciones de cadenas
Mensaje = 'hola ' + 'mundo ' + 'Python'
Men1=Mensaje.split()
Men2=' '.join(Men1)
print(Mensaje[0],Mensaje[0:4],Men1,Men2)
print(Mensaje.find("mundo"), Mensaje.lower())
# funciones de fecha
from datetime import datetime,timedelta,date
hoy, fdia = datetime.now(), date.today()
futuro = hoy + timedelta(days=30)
dif, aa, mm, dd = futuro, hoy.year, hoy.month, hoy.day
fecha = date(aa, mm, dd+2)
print(hoy, fdia, futuro, dif, fecha)