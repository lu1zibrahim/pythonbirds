class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}.'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):

    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return cumprimentar_da_classe + 'Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    luiz = Homem(nome="Otavio")
    pai = Pessoa(luiz, nome="Carlos", idade=74)
    print(Pessoa.cumprimentar(pai))
    print(id(pai))
    print(pai.cumprimentar())
    print(pai.nome)
    print(pai.idade)
    for filho in pai.filhos:
        print(filho.nome)
    pai.sobrenome = "Ibrahim"
    print(pai.sobrenome)
    del pai.filhos
    luiz.olhos = 1
    del luiz.olhos
    print(pai.__dict__)
    print(luiz.__dict__)
    print(Pessoa.olhos)
    print(pai.olhos)
    print(luiz.olhos)
    print(id(Pessoa.olhos), id(pai.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico(), luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luiz.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(luiz, Pessoa))
    print(isinstance(luiz, Homem))
    print(luiz.olhos)
    print(luiz.cumprimentar())
    print(pai.cumprimentar())

