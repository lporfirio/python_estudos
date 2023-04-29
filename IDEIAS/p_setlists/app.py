import ttkbootstrap as ttk


class Album:
    def __init__(self, nome, ano, artista, faixas):
        self.nome = nome
        self.ano = ano
        self.artista = artista
        self.faixas = faixas

    def exibirInformacoes(self):
        texto = f'''
    Nome: {self.nome}
    Ano: {self.ano}
    Artista: {self.artista}
    Faixas: {", ".join(self.faixas)}
    '''

        texto_inf["text"] = texto


def atualizar_album(event):
    album_selecionado = albuns_nomes.index(combobox.get())
    album_atual = albuns[album_selecionado]

    # Atualizar botões
    botao_inf.configure(command=album_atual.exibirInformacoes)


albuns = [
    Album('For Emma, Forever Ago', 2008, 'Bon Iver', [
        "Flume", "Lump Sum", "Skinny Love", "The Wolves (act I and II)", "Blindsided", "Creature Fear", "Team", "For Emma", "Re: Stacks"
    ]),
    Album("Everything's Fine", 2023, 'Matt Corby', [
        "Problems", "For Real", "Carry On", "Reeling'", "Big Smoke", "Lover", "Reruns", "Words I Say", "Mainies", "Better Than Thar", "Everythin's Fine"
    ]),
]

# MEU PROGRAMA
janela = ttk.Window()
janela.geometry("900x900")
janela.title('setlists de álbuns')

# criar a combobox com os nomes dos álbuns
albuns_nomes = [album.nome for album in albuns]
combobox = ttk.Combobox(janela, values=albuns_nomes)
combobox.grid(column=1, row=1, padx=70, pady=30)

combobox.bind("<<ComboboxSelected>>", atualizar_album)

# título
texto_album = ttk.Label(janela, text="álbuns: ")
texto_album.grid(column=1, row=0, padx=30, pady=10)
texto_album.config(font=("Arial", 20, "bold"))

# criar botões
botao_inf = ttk.Button(janela, text='Mostrar Informações',
                       command='', style="info")
botao_inf.grid(column=1, row=2, padx=10, pady=10)

botao_adicionar = ttk.Button(
    janela, text='Adicionar Novo Álbum', command='', style="info")
botao_adicionar.grid(column=1, row=3, padx=10, pady=10)


texto_inf = ttk.Label(janela, text='')
texto_inf.grid(column=1, row=4)


janela.mainloop()
