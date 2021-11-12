class Perro:

    anois = 10

       #instanciacion __init__ sirve para asignar valores
       #estos son los "atributos"
       #__init__ es un constructor o estado inicial

    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.__especie = "canino"
        #"encapsulacion" con 2 __ a la variable que quisieramos "anclar"

    #metodos
    #toda "accion" en el codigo vamos a llamarlo "metodos"

    def interactuar(self):
        print("el nombre del rrope es {}".format(self.nombre))

    def pelaje(self):
        print("su color es ", self.color)

    def tipo(self):
        print(f"su raza es {self.__especie}")

    def edad(self):
        if (self.anois > 20):
            print("es un perro viejito")
        else:
            print("todabia le queda hilo")


#instancia de clase
primerPerrito = Perro("Cuco", "Negro")

#no va a funcionar por que esta encapsulado
#inaccesible fuera del codigo
primerPerrito.especie = "felino"
primerPerrito.__especie = "felino"

primerPerrito.interactuar() #de esta manera conocemos su nombre objeto.metodo()
print(primerPerrito.nombre) #objeto.atributo


primerPerrito.pelaje()
primerPerrito.tipo()

primerPerrito.edad()


