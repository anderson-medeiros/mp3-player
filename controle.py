import tkinter as tk
from tkinter import ttk
from botao import Botao


class Controle(ttk.Frame):
    def __init__(self, conteiner):
        super().__init__(conteiner)
        self.criar_botoes()

    def criar_botoes(self):
        self.botao_anterior = self.criar_botao('./assets/arrow-left.png')
        self.botao_tocar = self.criar_botao('./assets/play.png')
        self.botao_proximo = self.criar_botao('./assets/arrow-right.png')
        botoes = self.winfo_children()
        for i, botao in enumerate(botoes):
            botao.grid_configure(row=0, column=i)

    def criar_botao(self, icone):
        botao = Botao(self, icone)
        return botao



raiz = tk.Tk()


controle = Controle(raiz)
controle.grid(row=0, column=0)



raiz.mainloop()
