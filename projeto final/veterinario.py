from agenda import *

class Usuario:
    def __init__(self, nome, **kwargs):
        super().__init__(**kwargs)
        self.nome = nome

class Veterinario(Usuario):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.agenda = Agenda()
