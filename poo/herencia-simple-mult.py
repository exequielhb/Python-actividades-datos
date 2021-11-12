
#Superclase o clase padre
class Vehiculos:

    #damos un estado inicial agregando como parametro marca y modelo
    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True
    
    def frenar(self):

        self.frena = True

    def estado(self):
        print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
         "\nAcelera", self.acelera, "\nFrena", self.frena)


class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            print("la furgoneta esta cargada")
        else:
            print("furgoneta vacia")


#heredamos atributos y metodos de la clase vehiculos
#podemos tener nuevos comportamientos, metodos atributos nuevos en la subclase o hijo
class Moto(Vehiculos):
    hwillie = "haciendo un willie"

    def willie(self):
        self.hwillie

    #sobreescribimos (sobreescritura de metodo) el metodo de la clase padre
    #esto pisa el codigo de la clase padre
    def estado(self):
        print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, 
        "\nAcelera", self.acelera, "\nFrena", self.frena, "\nwillie?", self.hwillie)


class VHelectricos():

    def __init__(self):
        self.autonomia = 100

    def carga_energia(self):
        self.cargando = True


#Herencias multiples
#se le da preferencia de la primera clase heredada
class Bicielectrica(VHelectricos, Vehiculos):
    pass



mimotito = Moto("Honda", "CBR")
mimotito.estado()

print("---------------- Separacion---------------------")

mifurgoneta = Furgoneta("Renault", "Kangoo")

mifurgoneta.arrancar()
mifurgoneta.estado()
mifurgoneta.carga(True)

print("---------------- Separacion---------------------")

mibici = Bicielectrica()

