import ttkbootstrap as ttk
import tkinter as tk

from lista_albuns import albuns
from class_album import Album


def adicionar_album():
    album = Album('', '', '', [])
    criar_janela(album)


def criar_janela(album):
    janela = ttk.Toplevel()
    janela.geometry("700x300")
    janela.title('Novo Álbum')

# criar as labels
    nome_label = ttk.Label(janela, text="Nome: ")
    nome_label.grid(column=0, row=0, padx=30, pady=10)
    ano_label = ttk.Label(janela, text="Ano: ")
    ano_label.grid(column=0, row=1, padx=30, pady=10)
    artista_label = ttk.Label(janela, text="Artista: ")
    artista_label.grid(column=0, row=2, padx=30, pady=10)
    faixas_label = ttk.Label(janela, text="Faixas (separadas por vírgula): ")
    faixas_label.grid(column=0, row=3, padx=30, pady=10)

# criar os campos de entrada
    nome_entry = ttk.Entry(janela, width=30, textvariable=tk.StringVar(value=album.nome))
    nome_entry.grid(column=1, row=0, padx=10, pady=10)
    ano_entry = ttk.Entry(janela, width=30, textvariable=tk.StringVar(value=album.ano))
    ano_entry.grid(column=1, row=1, padx=10, pady=10)
    artista_entry = ttk.Entry(janela, width=30, textvariable=tk.StringVar(value=album.artista))
    artista_entry.grid(column=1, row=2, padx=10, pady=10)
    faixas_entry = ttk.Entry(janela, width=30, textvariable=tk.StringVar(value=", ".join(album.faixas)))
    faixas_entry.grid(column=1, row=3, padx=10, pady=10)

# criar o botão de salvar
    botao_salvar = ttk.Button(janela, text='Salvar', command=lambda: salvar_album(album, nome_entry, ano_entry, artista_entry, faixas_entry, janela))
    botao_salvar.grid(column=1, row=4, padx=10, pady=10)

    janela.mainloop()

def salvar_album(album, nome_entry, ano_entry, artista_entry, faixas_entry, janela):
    album.nome = nome_entry.get()
    album.ano = ano_entry.get()
    album.artista = artista_entry.get()
    album.faixas = faixas_entry.get().split(", ")
    albuns.append(album) #adiciona o novo album na lista de álbuns
    print(albuns)
    janela.destroy()

