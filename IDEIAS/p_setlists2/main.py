import ttkbootstrap as ttk
from funcoes import Album
from lista_de_albuns import albuns



def atualizar_album(event):
    album_selecionado = albuns_nomes.index(combobox.get())
    album_atual = albuns[album_selecionado]
    texto_inf["text"] = album_atual.exibirInformacoes()


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

texto_inf = ttk.Label(janela, text='')
texto_inf.grid(column=1, row=4)

janela.mainloop()
