from .GameModels import Jogador

class Tela:
    # GameState??
    gameState = 'Something' 

    def __init__(self, width, height):
        self.width = width
        self.height = height


class TelaDoMenu(Tela):

    def __init__(self):
        self.background = bckgrnd
        super().__init__(w, h)

    # To be continued..

class TelaDaPartida(Tela):
    
    def __init__(self, w, h, bckgrnd):
        self.background = bckgrnd
        super().__init__(w, h)

    # To be continued..


class TelaDaPontuacao(Tela):

    def __init__(self):
        self.background = bckgrnd
        super().__init__(w, h)

    # To be continued..