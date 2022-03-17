import sqlite3
conn = sqlite3.connect('financeiro.db')

def criar_tabela():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS financeiro(
                        id_titulo INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_conta TEXT,
                        valor FLOAT,
                        data_vencimento DATE,
                        status TEXT,
                        data_pagamento DATE)''')
    except Exception as e:
        print("Erro na criação da tabela: ", e)

def add_titulo(nome_conta, valor, data_vencimento, status):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO financeiro (nome_conta, valor, data_vencimento, status) VALUES (?, ?, ?, ?)',(nome_conta, valor, data_vencimento, status))
        conn.commit()
        print('Adicionado com sucesso.')
    except sqlite3.Error as e:
        print("Erro ao inserir titulo: ", e)
    finally:
        cursor.close()

def get_titulo():
    try:
        return conn.execute('SELECT id_titulo, nome_conta, valor, data_vencimento, status, data_pagamento FROM financeiro')
    except sqlite3.Error as e:
        print("Erro ao buscar o titulo: ", e)

def excluir_titulo(id_titulo):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM financeiro WHERE id_titulo = ?',(id_titulo, ))
        conn.commit()
        conn.execute('VACUUM')
        print('Excluído com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao excluir titulo: ', e)
    finally:
        cursor.close()

def update_nome_titulo(id_titulo, nome_conta):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE financeiro set nome_conta = ? WHERE id_titulo = ?'''
        dado = (nome_conta, id_titulo)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()

def update_valor_titulo(id_titulo, valor):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE financeiro set valor = ? WHERE id_titulo = ?'''
        dado = (valor, id_titulo)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()
        
def update_vencimento_titulo(id_titulo, data_vencimento):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE financeiro set data_vencimento = ? WHERE id_titulo = ?'''
        dado = (data_vencimento, id_titulo)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()

def update_pagamento_titulo(id_titulo, data_pagamento):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE financeiro set data_pagamento = ? WHERE id_titulo = ?'''
        dado = (data_pagamento, id_titulo)
        cursor.execute(update_query, dado)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()
        
def update_pay_titulo(id_titulo, data_pagamento, status):
    try:
        cursor = conn.cursor()
        update_query1 = '''UPDATE financeiro set data_pagamento = ? WHERE id_titulo = ?'''
        update_query2= '''UPDATE financeiro set status = ? WHERE id_titulo = ?'''
        dado1 = (data_pagamento, id_titulo)
        dado2 = (status, id_titulo)
        cursor.execute(update_query1, dado1)
        cursor.execute(update_query2, dado2)
        conn.commit()
        print('Atualizado com sucesso.')
    except sqlite3.Error as e:
        print('Erro ao alterar aluno: ', e)
    finally:
        cursor.close()
        
