
from tkinter import *
from consts import *
from logica import *
import json


def create_coluna_esquerda(janela, lista_arquivos):
    # variaveis
    min_width = 300

    # Widgets
    coluna = Frame(janela, bg=cor_coluna1, padx=10, pady=10)
    listbox = Listbox(coluna)

    # Processos
    for arquivo in lista_arquivos:
        listbox.insert(END, arquivo)

    # Placement
    coluna.pack(side=LEFT, fill=BOTH, expand=True)
    listbox.pack(fill=BOTH, expand=True)

def create_coluna_centro(janela):
    coluna = Frame(janela, bg=cor_coluna2)
    coluna.pack(side=LEFT, fill=BOTH, expand=True)
    Entry(coluna, width=20).pack()

def create_coluna_direita(janela):
    coluna = Frame(janela, bg=cor_coluna3)
    coluna.pack(side=LEFT, fill=BOTH, expand=True)
    Button(coluna, text="Clique").pack()

def iniciar_janela(saves_folders):
    # Definindo a janela principal
    janela = Tk()
    janela.geometry("600x400")
    janela.minsize(width=600, height=400)
    janela.title("Saves & Backups")

    create_coluna_esquerda(janela, saves_folders)
    create_coluna_centro(janela)
    create_coluna_direita(janela)

    # Exibindo a janela
    janela.mainloop()

if __name__ == '__main__':
    saves_folders = verificar_pasta_salvar()
    iniciar_janela(saves_folders)