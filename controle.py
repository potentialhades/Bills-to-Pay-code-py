from modelo import MENU_INICIAL, TAMANHO, system_pause
import banco as bd
from estilo import cor
from modelo import exibir_cabecalho
from exececoes import leia_data, leia_nome, leia_valor, leia_numero

def exibir_titulo():
    for dado in bd.get_titulo():
        #condicao = u'\u2713' if dado[4] == 'Pago' else '\U0001F40D'
        condicao = cor(txt=str(dado[4]), cor='vermelho') if dado[4] == 'Pendente' else cor(txt=u'\u2713', cor='verde')
        d0 = cor(txt='\nID: ', cor='amarelo')+cor(txt=str(dado[0]), cor='amarelo')+'\t'
        d1 = cor(txt='Nome: ', cor='verde')+cor(txt=str(dado[1]), cor='verde')+'\t'
        d2 = cor(txt='Valor: ', cor='ciano')+cor(txt=str(dado[2]), cor='verde')+'\t'
        d3 = cor(txt='Vencimento: ', cor='ciano')+cor(txt=str(dado[3]), cor='verde')+'\t'
        d4 = cor(txt='Status: ', cor='ciano')+cor(txt=condicao.format(dado[4]), cor='verde')+'\t'
        d5 = cor(txt='Pagamento: ', cor='ciano')+cor(txt=str(dado[5]), cor='verde')
        imprime = d0+d1+d2+d3+d4+d5
        print(imprime)

def criar_titulo():
    try:
        nome_conta = leia_nome(cor(txt='Digite o nome da Conta: ', cor='verde'))
        valor = float(leia_valor(cor(txt='Digite o valor da Conta: ', cor='verde')))
        data_vencimento = leia_data(cor(txt='Digite a data do vencimento da Conta: ', cor='verde'))
        status = 'Pendente'
        print('Adicionando título -> ' + str(nome_conta))
    except Exception as e:
        print("Erro ao criar o título, {}".format(e))
    else:
        if nome_conta != str(MENU_INICIAL) and valor != str(MENU_INICIAL) and data_vencimento != str(MENU_INICIAL) and status != str(MENU_INICIAL):
            bd.add_titulo(nome_conta, valor, data_vencimento, status)
            system_pause()

def excluir_titulo():
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a ID do titulo: ', cor='amarelo'))
        print('Excluindo titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao excluir o titulo: {}".format(e))
    else:
        if id_titulo != MENU_INICIAL:
            bd.excluir_titulo(id_titulo)
        system_pause()
        
def alterar_nome_titulo():
    dado = 0
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a ID do titulo: ', cor='amarelo'))
        print('Alterando titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao alterar o titulo: {}".format(e))
    else:
        nome_conta = leia_nome(cor(txt='Digite o novo nome para a Conta: ', cor='verde'))
        if id_titulo != MENU_INICIAL:
            bd.update_nome_titulo(id_titulo, nome_conta)
            system_pause()

def alterar_valor_titulo():
    dado = 0
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a id do titulo: ', cor='amarelo'))
        print('Alterando valor titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao alterar o titulo: {}".format(e))
    else:
        valor = leia_valor(cor(txt='Digite o novo valor da Conta: ', cor='verde'))
        if id_titulo != MENU_INICIAL:
            bd.update_valor_titulo(id_titulo, valor)
        system_pause()

def alterar_vencimento_titulo():
    dado = 0
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a ID do titulo: ', cor='amarelo'))
        print('Alterando titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao alterar o titulo: {}".format(e))
    else:
        data_vencimento = leia_data(cor(txt='Digite o novo vencimento da Conta (formato AAAA-MM-DD): ', cor='verde'))
        if id_titulo != MENU_INICIAL:
            bd.update_vencimento_titulo(id_titulo, data_vencimento)
        system_pause()

def alterar_pagamento_titulo():
    dado = 0
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a ID do titulo: ', cor='amarelo'))
        print('Alterando titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao alterar o titulo: {}".format(e))
    else:
        data_pagamento = leia_data(cor(txt='Digite a nova data de pagamento da Conta (formato AAAA-MM-DD): ', cor='verde'))
        if id_titulo != MENU_INICIAL:
            bd.update_pagamento_titulo(id_titulo, data_pagamento)
        system_pause()

def pagar_titulo():
    dado = 0
    exibir_titulo()
    try:
        id_titulo = leia_numero(cor(txt='Digite a ID do titulo: ', cor='amarelo'))
        print('Pagando titulo -> ' + str(id_titulo))
    except Exception as e:
        print("Erro: Ao pagar o titulo: {}".format(e))
    else:
        data_pagamento = leia_data(cor(txt='Digite a data de pagamento da Conta (formato AAAA-MM-DD): ', cor='verde'))
        status = 'Pago'
        if id_titulo != MENU_INICIAL:
            bd.update_pay_titulo(id_titulo, data_pagamento, status)
        system_pause()