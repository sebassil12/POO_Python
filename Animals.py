class Perro():
    def sonido(self):
        print("Guau")

class Gato():
    def sonido(self):
        print("Miau ")

def animal_sound(animal):
    animal.sonido()
    pass

gato = Gato()
perro = Perro()

animal_sound(gato)