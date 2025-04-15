from datetime import  datetime
class Otaku:
    def __init__(self, nombre:str, estilo:str):
        self.nombre=nombre
        self.estilo=estilo

    def getInfo(self)-> None:
        print(f"{self.nombre} es de estilo {self.estilo}")



manga: Otaku = Otaku("Dragon Ball","Shonen")

name = "David"
age = 31


def presentacion()-> None:
    print("Hola, me llamo: ", name,",  mi edad es: ", age," y son las: ",datetime.now())

presentacion()

def greeting(name:str, age:int)->None:
    print(f"Hello, my name is: {name}, and my age is {age}!")

greeting("David",31)

def sumar(valor1:int, valor2:int)-> int:
    print(f"La suma de los 2 valores es: {valor1+valor2}")

sumar(1,3)

manga.getInfo()