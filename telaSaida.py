from tkinter import *
import psycopg2 as psc

def conectar():
    conn = psc.connect(host = "200.129.44.249",
     database = "510613",
     user = "510613",
     password = "510613@fbd")
    return conn

def consultar():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("select * from aluno")
    resultado = cur.fetchall()
    cur.close()
    conn.close()
    return resultado

root = Tk()
root.title("Primeira Janela Criada")
root.geometry("800x600")
root.resizable(False, False)

result = consultar()

for i in range(len(result)):
    for j in range(6):
        e = Label(root, fg='blue',font=('Arial',10,'bold'), width = 10,text = str(result[i][j]), borderwidth = 1, relief = "solid", anchor = "e")
        e.grid(row = i, column = j)
        print(result[i][j])
root.mainloop()