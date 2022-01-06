class Mamifero(object):
    def __init__(self, cor_de_pelo, genero, andar):
        self.cor_de_pelo = cor_de_pelo
        self.genero = genero
        self.num_de_patas = andar

    def falar(self):
        print('Olá sou um mamifere e eu sei falar')
    def andar(self):
        print('Estou andando sobre %i patas', self.num_de_patas)
    def amamentar(self):
        if self.genero.lower() [0] == 'm':
            return
        print('Amamentado meu filhote')