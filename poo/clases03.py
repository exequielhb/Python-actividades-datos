class Coche:
    
    #Constructor Init
    #encapsulamiento con __
    def __init__(self):
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancar):
        self.__enmarcha = arrancar

        if (self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "el coche esta en marcha"
        elif (self.__enmarcha and chequeo == False):
            return "algo anda mal en el chequeo, no podemos arrancar"
        else:
            return "el coche esta parado"
    
    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas, un ancho de ", self.__ancho_chasis, " y un largo de ", 
        self.__largo_chasis)

    #chequeamos la condicion del auto


    #metodo encapsulado, solamente se puede utilizar desde dentro de la clase
    def __chequeo_interno(self):
        print("realizando un analisis del vehiculo")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return "todo correcto"
        else:
            return "algo anda mal"






mi_coche = Coche()

print(mi_coche.arrancar(False))
mi_coche.estado()

print("-------- Aca creamos el segundo objeto -------------------")

mi_coche2 = Coche()

#necesitamos un parametro para arrancar
print(mi_coche2.arrancar(True))
mi_coche2.estado()
