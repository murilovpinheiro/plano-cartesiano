import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import psycopg2 as psc

def conectar():
    conn = psc.connect(host = "200.129.44.249",
     database = "510613",
     user = "510613",
     password = "510613@fbd")
    return conn

def inserir():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO aluno(nome, sexo, data_nasc, endereco, email) values (%s, %s, %s, %s, %s);", (nomeS.get(), sexoS.get(), dataS.get(), endS.get(), emailS.get()))
        conn.commit()
        showinfo("Aviso: ", "Salvou")
    except Exception as e:
        showinfo("ERRO","Dados Digitados são Inválidos")
        if (str(e).find("invalid input syntax for type integer") )> -1:
            print("Valor Digitado Inválido")
    cursor.close()
    conn.close()


root = tk.Tk()
root.title("Primeira Janela Criada")
root.geometry("600x450")
root.resizable(False, False)

frame = ttk.Frame(root)
frame.pack(padx = 10, pady = 0, fill = "x", expand = True)

nome = ttk.Label(frame, text = "Nome: ")
sexo = ttk.Label(frame, text = "Sexo: ")
data = ttk.Label(frame, text = "Data de Nascimento: ")
end = ttk.Label(frame, text = "Endereço: ")
email = ttk.Label(frame, text = "Email: ")

nomeS = tk.StringVar()
sexoS = tk.StringVar()
dataS = tk.StringVar()
endS = tk.StringVar()
emailS = tk.StringVar()

nomeEntrada = ttk.Entry(frame, textvariable = nomeS)
sexoEntrada = ttk.Entry(frame, textvariable = sexoS)
dataEntrada = ttk.Entry(frame, textvariable = dataS)
endEntrada = ttk.Entry(frame, textvariable = endS)
emailEntrada = ttk.Entry(frame, textvariable = emailS)

nome.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
nomeEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

sexo.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
sexoEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

data.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
dataEntrada.pack(expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

end.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
endEntrada.pack(expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

email.pack( expand = True, pady = 10, side = tk.TOP, anchor = tk.CENTER)
emailEntrada.pack( expand = True, side = tk.TOP, anchor = tk.CENTER, ipadx = 50)

button = ttk.Button(frame, text = "Pesquisar", command = inserir)
button.pack( expand = True, pady = 25, anchor = tk.CENTER)

root.mainloop()