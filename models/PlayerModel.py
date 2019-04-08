from .GameModels import *

class Jogador:
    pontuacao = 0

    def __init__(self, apelido):
        self.apelido = apelido
        self.suporte = Suporte()

    def mostraSuporte(self):
        return self.suporte.retornaSuporte()

    def atribuiSuporte(self, pecasSuporte):
        self.suporte = pecasSuporte

    def atribuiPontuacao(self, valor):
        self.pontuacao = valor

    def compraPecaMonte(self, monte):
        self.suporte.compraPeca(monte)

    def somaValoresSuporte(self):
        return self.suporte.somaValoresSuporte()

    # Modo: 1 => Sequencia de cores iguais
    #       2 => Grupos de cores diferentes
    def ordenaSuporte(self, modo):
        if(modo == 1 or modo == 2):
            self.suporte.ordenaPecas(modo)

    # Need to implement
    def calculaPontuacao(self):
        pass


class Jogadores:

    def __init__(self):
        self.jogadores = list()

    def retornaJogadores(self):
        return self.jogadores

    def retornaPosicao(self, j):
        return self.jogadores.index(j)

    def retornaJogador(self, posicao):
        return self.jogadores[posicao]

    def adcionaJogador(self, j):
        self.jogadores.append(j)

    def removeJogador(self, j):
        return self.jogadores.pop(self.retornaPosicao(j))