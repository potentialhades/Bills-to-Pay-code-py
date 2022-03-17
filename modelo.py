import banco as bd
from estilo import cor

MENU_INICIAL = 99
TAMANHO = 60

def exibir_cabecalho(*opcs):
    """ Imprimir o cabeçalho no terminal utilizando com no minimo 60 chars """
    print('-' * TAMANHO)
    print("{:^60}".format(cor(txt='CADASTROS', cor='azul')))
    for n, item in enumerate(opcs, start=1):
        print('|', f"{cor(txt=n, cor='amarelo')} - {cor(txt=item, cor='ciano')}".ljust(55), '|')
    print('-' * TAMANHO)
    opc = int(input(cor(txt='Opção: ', cor='amarelo')))
    while opc not in range(1, len(opcs) + 1):
        if opc not in range(1, len(opcs) + 1):
            print(cor(txt='ERRO: Digite uma opção válida{}'.format(opc), cor='vermelho'))
            opc = int(input(cor(txt='Opção: ', cor='amarelo')))
    return opc

def system_pause():
    return_menu = input('\nAperte "Enter" do teclado para Retornar ao Menu CADASTROS. ')
    while return_menu == '':
        break