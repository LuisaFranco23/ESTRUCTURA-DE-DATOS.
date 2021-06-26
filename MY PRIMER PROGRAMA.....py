num=10
num= "20"
if type(num)==int:
    num=num*2
else:
    print("el valor no es un numerico")

def mensaje(msg):
    print(msg)



    mensaje("bienviendido a pyton")
    mensaje("mi primer programa")


class sintaxis:

    def __init__(self,dato="instancia de la clase" ):
        self.frase=dato



    def usovariable(self):
        edad,peso= 21, 30.5
        nombres:"LUISA FRANCO"
        tipo_de_sexo: "f"
        civil:True
           #print("civil={}y su tipo es:{}",format(civil,type(civil)))
        usuario=()
        usuario=("luisa","1234","luisa@gmail.com",True)
        #             0      1      2             3
        x=usuario[0]
        materia=["programacion web","php","poo"]
        materia.append("go")

        estudiante={}
        estudiante={"nombre":"Luisa","edad":21,"fac":"faci",}
        estudiante["edad"]=21
        #print(materia,materia[2:],materia[:2],mateia[:-1],materia[-2:])
        print("x,y")
        print(estudiante,estudiante["nombre"])
    def mostrar(self):
        print("mostrar")
        print(self.frase)

ejercicio=sintaxis()
ejercicio.usovariable()




