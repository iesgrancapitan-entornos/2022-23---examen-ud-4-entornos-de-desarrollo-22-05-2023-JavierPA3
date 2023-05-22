"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:

    def __init__(self) :
        self.ladrar = 'Guau'

    def ladrar(self):
        print(self.ladrar);

p = Perro();
p.ladrar();
