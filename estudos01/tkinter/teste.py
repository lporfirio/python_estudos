from tkinter import *
from tkinter import ttk


class Carro:
    def __init__(self, cor, marca, modelo, ano):
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        texto = f'Ligando o {self.modelo}'

        texto_ligar["text"] = texto

    def desligar(self):
        texto = f'Desligado o {self.modelo}'

        texto_desligar["text"] = texto


    def exibirInformacoes(self):
        texto = f'Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}'

        texto_inf["text"] = texto
     

def atualizar_carro(event):
    carro_selecionado = carros_marcas.index(combobox.get())
    carro_atual = carros[carro_selecionado]

    # Atualizar botões
    botao_ligar.configure(command=carro_atual.ligar)
    botao_desligar.configure(command=carro_atual.desligar)
    botao_inf.configure(command=carro_atual.exibirInformacoes)


carros = [    
    Carro('Vermelho', 'Ferrari', 'SP51', 2023),    
    Carro('Cinza', 'Fiat', 'Uno', 2020),    
    Carro('Preto', 'Volkswagen', 'Gol', 2019),    
    Carro('Branco', 'Ford', 'Fiesta', 2021),    
    Carro('Azul', 'Renault', 'Sandero', 2018)]


#MEU PROGRAMA
janela = Tk()
janela.title('gerenciador de tarefas')



# criar a combobox com os modelos de carros
carros_marcas = [carro.marca for carro in carros]
combobox = ttk.Combobox(janela, values=carros_marcas)
combobox.grid(column=0, row=0, padx=50, pady=10)

combobox.bind("<<ComboboxSelected>>", atualizar_carro)

# criar botões

botao_ligar = Button(janela, text='Ligar')
botao_ligar.grid(column=0, row=1, padx=15, pady=10)

texto_ligar = Label(janela, text='')
texto_ligar.grid(column=0, row=2, padx=15, pady=10)

botao_desligar = Button(janela, text='Desligar')
botao_desligar.grid(column=0, row=3, padx=15, pady=10)

texto_desligar = Label(janela, text='')
texto_desligar.grid(column=0, row=4, padx=15, pady=10)

botao_inf = Button(janela, text='Informacões')
botao_inf.grid(column=0, row=5, padx=15, pady=10)

texto_inf = Label(janela, text='')
texto_inf.grid(column=0, row=6, padx=15, pady=50)




janela.mainloop()
