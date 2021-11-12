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


#heredamos atributos y metodos de la clase vehiculos
class Moto(Vehiculos):
    pass

mimotito = Moto("Honda", "CBR")
mimotito.estado()