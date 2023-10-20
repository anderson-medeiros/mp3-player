import tkinter as tk
from tkinter import ttk


class Botao(ttk.Button):
    def __init__(self, conteiner, icone=None):
        super().__init__(conteiner)

        if icone:
            self.icone = tk.PhotoImage(file=icone)
            self.config(image=self.icone)

