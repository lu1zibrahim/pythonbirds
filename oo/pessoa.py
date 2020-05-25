class Pessoa():


    olhos = 2
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
    luiz.olhos = 1
    del luiz.olhos
    print(carlos.__dict__)
    print(luiz.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luiz.olhos)
    print(carlos.olhos)
    print(id(Pessoa.olhos),id(carlos.olhos), id(luiz.olhos))