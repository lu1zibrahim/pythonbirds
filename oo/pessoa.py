class Pessoa:
    def __init__(self,*filhos, nome = None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    luiz = Pessoa(nome="Luiz")
    pai = Pessoa(luiz, nome="Carlos", idade=74)
    print(Pessoa.cumprimentar(pai))
    print(id(pai))
    print(pai.cumprimentar())
    print(pai.nome)
    pai.nome = "Luiz Carlos"
    print(pai.nome)
    print(pai.idade)
    for filho in pai.filhos:
        print(filho.nome)
    print(pai.filhos)