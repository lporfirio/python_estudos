class Carro:
    def __init__(self, cor, modelo, ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print(f'Ligando o {self.modelo}')

    def desligar(self):
        print(f'Desligado o {self.modelo}')

    def exibirInformacoes(self):
        print(f'Cor: {self.cor}\nModelo: {self.modelo}\nAno: {self.ano}')



ferrari = Carro('Vermelho', 'SP51', 2023)

ferrari.ligar()
ferrari.desligar()
ferrari.exibirInformacoes()
