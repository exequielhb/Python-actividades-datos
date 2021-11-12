#clase es el modelo, donde se redactar caracteristicas comunes de un grupo de "objetos"

#ejemplar,
#modularizacion - diferentes clases
#encapsulamiento - una clase tiene una funcion independiente pero todas funcionan en conjunto

#clase
class Coche():

    #propiedad
    largo = 250
    ancho = 120
    ruedas = 4
    enmarcha = False

    #comportamientos o metodos(que es capas de hacer)
    #lo creamos con la palabra reservada "def"
        #nombre de la funcion "self", hace referencia al objeto perteneciente a la clase
    def arrancar(self):
        self.enmarcha = True
    
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return "el coche esta parado"


#aca instanciamos,creamos o ejemplarizamos la clase!!
miCoche=Coche()

#nomenclatura del punto, nombre del objeto=miCoche y propiedad
print("el largo del coche es: ", miCoche.largo)
print("el auto esta en marcha? ", miCoche.enmarcha)
print("el auto tiene: ", miCoche.ruedas, "ruedas")


#preguntamos si esta en marcha, antes debemos arrancar xD
miCoche.arrancar()
print(miCoche.estado())