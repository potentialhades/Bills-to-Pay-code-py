from estilo import cor

def leia_numero(numero):
    while True:
        try:
            numero = int(input(numero))
        except (ValueError, TypeError):
            print(cor(txt = 'ERRO: Por favor, digite um inteiro válido.', cor = 'vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um inteiro válido. {}'.format(ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt = f'ERRO: {e.__cause__}', cor = 'vermelho'))
        else:
            return numero


def leia_valor(valor):
    while True:
        try:
            valor = float(input(valor))
            while valor < 0:
                print(cor(txt='ERRO: Por favor digite um valor valido', cor = 'vermelho'))
                valor = float(input(valor))
        except (ValueError, TypeError):
            print(cor(txt='ERRO: Por favor, digite um valor válido.', cor='vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um valor válido. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return valor


def leia_nome(nome_conta):
    while True:
        try:
            nome_conta = str(input(nome_conta))
            while nome_conta == ' ' or nome_conta == '':
                print(cor(txt='ERRO: Por favor digite um nome válido', cor = 'vermelho'))
                nome_conta = str(input(nome_conta))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um nome válido. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
            print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return nome_conta

def leia_data(data):
    while True:
        try:
            data = str(input(data))
            separador = '-'
            while separador not in data:
                print(cor(txt='ERRO: Por favor, digite uma data válida utilizando " - " como separador (formato: AAAA-MM-DD).', cor='vermelho'))
                data = str(input(data))
            dado = data.split(sep='-')
            mes, dia = dado[1], dado[2]
            while not '0'<dia<='31':
                print(cor(txt='ERRO: Por favor, digite uma data válida utilizando " - " como separador (formato: AAAA-MM-DD).', cor='vermelho'))
                data = str(input(data))
                dado = data.split(sep='-')
                mes, dia = dado[1], dado[2]
            while not '0'<mes<='12':
                print(cor(txt='ERRO: Por favor, digite uma data válida utilizando " - " como separador (formato: AAAA-MM-DD).', cor='vermelho'))
                data = str(input(data))
                dado = data.split(sep='-')
                mes, dia = dado[1], dado[2]
            while mes=='02' and dia>='30':
                print(cor(txt='ERRO: Por favor, digite uma data válida utilizando " - " como separador (formato: AAAA-MM-DD).', cor='vermelho'))
                data = str(input(data))
                dado = data.split(sep='-')
                mes, dia = dado[1], dado[2]
        except (ValueError, TypeError):
            print(cor(txt = 'ERRO: Por favor, digite um inteiro válido.', cor = 'vermelho'))
        except KeyboardInterrupt as ki:
            print(cor(txt='ERRO: Por favor, digite um dia válido. {}'.format(
                ki), cor='vermelho'))
        except Exception as e:
                print(cor(txt=f'ERRO: {e.__cause__}', cor='vermelho'))
        else:
            return data
