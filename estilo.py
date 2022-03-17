cores = {
    '': '\033[m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'azul': '\033[1;34m',
    'ciano': '\033[1;36m',
    'magenta': '\033[1;35m',
    'amarelo': '\033[1;33m',
    'preto': '\033[1;30m',
    'branco': '\033[1;37m',
    'restaura_cor_original': '\033[1;0;0m',
    'negrito': '\033[1;1m',
    'reverso': '\033[1;2m',
    'fundo_preto': '\033[1;40m',
    'fundo_vermelho': '\033[1;41m',
    'fundo_verde': '\033[1;42m',
    'fundo_amarelo': '\033[1;43m',
    'fundo_azul': '\033[1;44m',
    'fundo_magenta': '\033[1;45m',
    'fundo_ciano': '\033[1;46m',
    'fundo_branco': '\033[1;47m'
}


def cor(txt='', cor=''):
    return f'{cores[cor]}{txt}{cores[""]}'
