class Pessoa():
    def __init__(self,*filhos, nome="None",idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luiz = Pessoa(nome='Luiz')
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
    print(carlos.__dict__)
    print(luiz.__dict__)