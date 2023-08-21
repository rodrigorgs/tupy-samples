#!/usr/bin/env python3
from tupy import *

class Espiral(Image):
    pass

class Campo(Image):
    def __init__(self):
        self.file = 'campo.png'
        self.x = 320
        self.y = 240

# https://pokemondb.net/sprites
class Pokemon(Image):
    def __init__(self, file, x, y):
        self._vida = 100
        self._forca = 30
        self.file = file
        self.x = x
        self.y = y
        self._label = Label("", self.x - 50, self.y + 50)
        self._atualiza_label()

    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self, value):
        self._vida = value
        self._atualiza_label()

    @property
    def forca(self):
        return self._forca
    @forca.setter
    def forca(self, value):
        self._forca = value
        self._atualiza_label()
        
    def _atualiza_label(self):
        self._label.text = f"Vida: {self._vida}\nForça: {self._forca}"

    def ataca(self, pokemon):
        if self._vida <= 0:
            toast('O pokémon está desmaiado!')
        else:
            pokemon.recebe_dano(self._forca)
        
    def recebe_dano(self, dano):
        if self._vida <= 0:
            toast('O pokémon está desmaiado!')
            return
        self._vida -= dano
        if self._vida <= 0:
            self._vida = 0
            self.desmaia()
        self._atualiza_label()

    def desmaia(self):
        toast('O pokémon desmaiou!')
        self._vida = 0
        self._atualiza_label()
        self.espiral = Espiral()
        self.espiral.x = self.x
        self.espiral.y = self.y

    def pode_ser_capturado(self):
        return 0 < self._vida <= 20

    def evolui(self):
        if self._vida <= 0:
            toast('O pokémon está desmaiado!')
            return
        self._vida += 10
        self._forca += 10
        if self.file == 'pikachu.png':
            self.file = 'raichu.png'
        elif self.file == 'charmander.png':
            self.file = 'charmeleon.png'
        elif self.file == 'charmeleon.png':
            self.file = 'charizard.png'
        elif self.file == 'bulbasaur.png':
            self.file = 'ivysaur.png'
        elif self.file == 'ivysaur.png':
            self.file = 'venusaur.png'
        else:
            self._vida -= 10
            self._forca -= 10
        self._atualiza_label()
    

class Pokeball(Image):
    def __init__(self):
        self.conteudo = None

    def joga(self, pokemon):
        if self.conteudo:
            toast('A pokeball já está cheia!')
        elif pokemon.vida <= 0:
            toast('O pokémon está desmaiado!')
        elif pokemon.pode_ser_capturado():
            self.conteudo = pokemon
            pokemon._hide()
            pokemon._label._hide()
            toast('Pokémon capturado!')
        else:
            toast('O pokémon se esquivou!')

if __name__ == '__main__':
    campo = Campo()

    pikachu = Pokemon('pikachu.png', 200, 300)
    charmander = Pokemon('charmander.png', 400, 300)

    pokeball = Pokeball()
    pokeball.file = 'pokeball.png'
    pokeball.x = 300
    pokeball.y = 150

    run(globals())
