class Persona:

    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    
    def getInfo(self)->None:
        print(f"El nombre de la persona es {self.nombre} y la edad es {self.edad}")

    def duplicar(self)->int:
        print(f"La edad duplicada es {self.edad+self.edad}")

    def sumar(self,var1,var2)->None:
        print(f"La suma de las variables es igual a: {var1+var2}")

    def set(self, newEdad, newName):
        self.nombre=newName
        self.edad=newEdad

    def getNewValores(self):
        print(f"Los nuevos valores para la edad y el nombre son: {self.edad} y {self.nombre}")

class Objeto:
    def __init__(self):
        pass
    def test(self):
        print("Esto es una prueba")
    def english(self):
        print("This is a test")



David: Persona = Persona("David",31)
David.getInfo()
David.duplicar()
David.sumar(2,3)

Daniel: Persona =Persona("Daniel", 40)
Daniel.getInfo()
Daniel.sumar(10,20)

cosa: Objeto = Objeto()
cosa.test()

thing = Objeto()
thing.english()

David.set(50,"Goku")
David.getNewValores()
David.getInfo()