# Superclasse Pokemon
class Pokemon:

    def __init__(self,nome,tipo,ataque,defesa):

        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa


# Subclasses Pokemon
class PokemonTerra(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)

class PokemonAgua(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)
        
class PokemonAr(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)

class PokemonFogo(Pokemon):

    def __init__(self, nome, tipo, ataque, defesa):
        super().__init__(nome, tipo, ataque, defesa)


# Superclasse Treinador
class Treinador:

    def __init__(self,nome) -> None:
        pass
        