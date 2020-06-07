class Pessoa():


    olhos = 2
    def __init__(self,*filhos, nome="None",idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'



class Homem(Pessoa):
    pass


if __name__ == '__main__':
    luiz = Homem(nome='Luiz')
    carlos = Pessoa(luiz,nome="Carlos")
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome = "Ibrahim"
    del carlos.filhos
    luiz.olhos = 1
    del luiz.olhos
    print(carlos.__dict__)
    print(luiz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(carlos.olhos)
    print(id(Pessoa.olhos),id(carlos.olhos), id(luiz.olhos))
    print(Pessoa.metodo_estatico(), luiz.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(),luiz.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(luiz, Pessoa))
    print(isinstance(luiz, Homem))
