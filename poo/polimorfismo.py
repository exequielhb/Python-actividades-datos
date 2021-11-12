class Coche():

    def desplazamiento(self):
        print("Me muevo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me muevo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me muevo utilizando 6 ruedas")


#recibimos un objeto por parametro

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()


#almacenamos mivehiculo de la clase camion 
mivehiculo = Camion()
desplazamiento_vehiculo(mivehiculo)









""" mivehiculo = Moto()
mivehiculo.desplazamiento()

mivehiculo2 = Coche()
mivehiculo2.desplazamiento()

mivehiculo3 = Camion()
mivehiculo3.desplazamiento() """