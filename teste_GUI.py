#=====================================BIBLIOTECAS==============================================
from tkinter import Tk, Frame, TOP, StringVar, SOLID, LEFT, RIGHT, X, Y, Label, Entry, Button, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, NO, W
import sqlite3
import tkinter.ttk as ttk
#=====================================TELA==============================================
root = Tk()
root.title('Pesquisa de Cadastro de Títulos')
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
#=====================================METODOS==============================================
def base_de_dados():
    conn = sqlite3.connect('financeiro.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM financeiro ORDER BY nome_conta ASC''')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def pesquisar():
    if procura.get() != '':
        tree.delete(*tree.get_children())
        conn = sqlite3.connect('financeiro.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM financeiro WHERE nome_conta LIKE ? OR data_vencimento LIKE ?''',
                       ('%'+str(procura.get())+'%', '%'+str(procura.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def limpa():
    conn = sqlite3.connect('financeiro.db')
    cursor = conn.cursor()
    tree.delete(*tree.get_children())
    cursor.execute('''SELECT * FROM financeiro ORDER BY nome_conta ASC''')
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
#=====================================VARIAVEIS============================================
procura = StringVar()
#=====================================FRAME================================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
TopFrame = Frame(root, width=800)
TopFrame.pack(side=TOP)
TopForm = Frame(TopFrame, width=800)
TopForm.pack(side=LEFT, pady=10)
TopMargin = Frame(TopFrame, width=260)
TopMargin.pack(side=LEFT)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)
#=====================================LABEL =========================================
lbl_title = Label(Top, width=500, font=('arial', 18),
                  text='Filtro de Pesquisa')
lbl_title.pack(side=TOP, fill=X)
#=====================================ENTRY =========================================
procura = Entry(TopForm, textvariable=procura)
procura.pack(side=LEFT)
#=====================================BUTTON ========================================
btn_procura = Button(TopForm, text='Pesquisar', bg="#006dcc", command=pesquisar)
btn_procura.pack(side=LEFT)
btn_limpar = Button(TopForm, text='Limpar', command=limpa)
btn_limpar.pack(side=LEFT)
#=====================================TABELA =========================================
scrollbarx = Scrollbar(MidFrame, orient=HORIZONTAL)
scrollbary = Scrollbar(MidFrame, orient=VERTICAL)
tree = ttk.Treeview(MidFrame, columns=('id_titulo', 'nome_conta', 'valor', 'data_vencimento', 'status', 'data_pagamento'),
                    selectmode='extended', height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('id_titulo', text='id_titulo', anchor=W)
tree.heading('nome_conta', text='Nome', anchor=W)
tree.heading('valor', text='Valor', anchor=W)
tree.heading('data_vencimento', text='Data Vencimento', anchor=W)
tree.heading('status', text='Status', anchor=W)
tree.heading('data_pagamento', text='Data Pagamento ', anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
#=====================================INICIA=======================================
if __name__ == '__main__':
    base_de_dados()
    root.mainloop()