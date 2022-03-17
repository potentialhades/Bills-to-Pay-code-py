from controle import criar_titulo, exibir_titulo, alterar_nome_titulo, alterar_valor_titulo, alterar_vencimento_titulo, alterar_pagamento_titulo, pagar_titulo
from modelo import exibir_cabecalho
from controle import excluir_titulo, alterar_nome_titulo, exibir_cabecalho

def main():
    while True:
        try:
            escolha = exibir_cabecalho('Adicionar titulo', 'Exibir titulo(s)', 'Excluir titulo', 'Alterar nome titulo', 'Alterar valor titulo', 'Alterar vencimento titulo', 'Alterar pagamento titulo', 'Pagar titulo','Sair')
        except Exception:
            print('Erro!')
        else:
            if escolha == 1:
                criar_titulo()
            elif escolha == 2:
                exibir_titulo()
            elif escolha == 3:
                excluir_titulo()
            elif escolha == 4:
                alterar_nome_titulo()
            elif escolha == 5:
                alterar_valor_titulo()
            elif escolha == 6:
                alterar_vencimento_titulo()
            elif escolha == 7:
                alterar_pagamento_titulo()
            elif escolha == 8:
                pagar_titulo()
            elif escolha == 9:
                break
            else:
                print('Opção invalida')