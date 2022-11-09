import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter.messagebox import showinfo

arquivo = pd.read_csv("./exemplo.csv")

def pesquisarPessoa():
    showinfo("Pesquisa", (arquivo.loc[(arquivo.id == int(pesquisa.get()))])["nome"].item())
    

root = tk.Tk()
root.title("Primeira Janela Criada")
root.geometry("300x150")
root.resizable(False, False)

frame = ttk.Frame(root)
frame.pack(padx = 10, pady = 0, fill = "x", expand = True)

texto1 = ttk.Label(frame, text = "Pesquise por ID: ")


pesquisa = tk.StringVar()
pesquisaEntrada = ttk.Entry(frame, textvariable = pesquisa)
texto1.pack(fill = tk.X, expand = True, pady = 10, side = tk.TOP)
pesquisaEntrada.pack(fill = tk.X, expand = True, side = tk.LEFT)

button = ttk.Button(frame, text = "Pesquisar", command = pesquisarPessoa)
button.pack(fill = tk.X, expand = True, pady = 10, side = tk.BOTTOM)

root.mainloop()