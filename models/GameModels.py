from .PieceModels  import *

class Monte:

    def __init__(self):
        # no inicio, o monte contém todas as peças do jogo
        self.montePecas = Pecas()

    def embaralhaMonte(self):
        self.montePecas.embaralhaPecas()

    def atribuiPecasMonte(self, pecas):
        self.montePecas = pecas

    def contaPecasMonte(self):
        return self.montePecas.contaPecas()

    def removePecaAleatoria(self):
        p = self.montePecas.removePecaAleatoria()
        return self.montePecas.removePeca(p)

    def retornaMonte(self):
        return self.montePecas.retornaPecas()

class Suporte:

    def __init__(self):
        self.listaPecas = Pecas()

    def compraPeca(self, monte):
        p = monte.removePecaAleatoria()
        self.listaPecas.adcionaPeca(p)

    def atribuiPecasSuporte(self, pecas):
        self.listaPecas = pecas

    def removePeca(self, p):
        return self.listaPecas.removePeca(p)

    def contaPecasSuporte(self):
        return self.listaPecas.contaPecas()

    def retornaSuporte(self):
        return self.listaPecas.retornaPecas()

    def somaValoresSuporte(self):
        return self.listaPecas.somaValoresPecas()

    # Need to implement
    def ordenaPecas(self, modo):
        self.listaPecas.ordenaPecas(modo)

        
class Mesa:
    turnos = 0

    def __init__(self, jogadores, monte):
        self.jogadores = jogadores
        self.monte = monte
    
    


