import random

class Peca:
    def __init__(self, valor, img):
        self.valor = valor
        self.img = img


class Pecas:
    def __init__(self):
        self.pecas = list()

    def retornaPosicao(self, peca):
        return self.pecas.index(peca)

    def retornaPeca(self, posicao):
        return self.pecas[posicao]

    def retornaPecas(self):
        return self.pecas

    def adcionaPeca(self, p):
        self.pecas.append(p)

    def removePeca(self, p):
        return self.pecas.pop(self.retornaPosicao(p))

    def contaPecas(self):
        return len(self.retornaPecas())

    def removePecaAleatoria(self):
        random.seed()
        return random.choice(self.pecas)

    def embaralhaPecas(self):
        random.shuffle(self.pecas)

    def somaValoresPecas(self):
        return sum(list(map(lambda x: x.valor, self.pecas)))

    def ordenaPecas(self, modo):
        if(modo == 1):
            self.pecas = sorted(self.pecas, key=lambda x: (x.cor, x.valor))
        if(modo == 2):
            self.pecas = sorted(self.pecas, key=lambda x: x.valor)

    def esvaziar(self):
        self.pecas.clear()


class PecaCuringa(Peca):
    cor = 'void'

    def __init__(self, valor, img):
        super().__init__(valor, img)


class PecaAzul(Peca):
    cor = 'azul'

    def __init__(self, valor, img):
        super().__init__(valor, img)
    pass


class PecaAmarela(Peca):
    cor = 'amarela'
    
    def __init__(self, valor, img):
        super().__init__(valor, img)
    pass


class PecaPreta(Peca):
    cor = 'preta'
    
    def __init__(self, valor, img):
        super().__init__(valor, img)
    pass


class PecaVerde(Peca):
    cor = 'verde'
    
    def __init__(self, valor, img):
        super().__init__(valor, img)
    pass


