#aca vemos 2 instrucciones super() e isinstance()

class Persona:
    
    def __init__(self, nombre, edad, lugar_residencia):

        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("nombre {}".format(self.nombre))
        print("edad {}".format(self.edad))
        print("residencia {}".format(self.lugar_residencia))



class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        #lo que hace es ejecutar enteramente el constructor init de la clase padre
        #pasamos esos atributos dentro de init, estos son valores fijos
        #super().__init__("Exequiel", 25, "Argentina")
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)
        

Elempleado = Empleado(1500, 15, "Marcos", 33, "Ecuador")

Elempleado.descripcion()
    
#isinstance nos sirve para saber si pertenece a una clase en concreto
#con TRUE OR FALSE
#                   obejto    clase
#principio de sustitucion
print(isinstance(Elempleado, Empleado))
print(isinstance(Elempleado, Persona))