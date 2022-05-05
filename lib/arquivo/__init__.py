from string import ascii_lowercase

vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'

#verifica se o arquivo existe
def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

#cria um arquivo
def arquivoCriar(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print('falha ao criar arquivo')
    else:
        a.close()
        print(f'arquivo {arquivo} criado com sucesso')

#registra palavras
def registrarPalavra(arquivo):
    validos = ascii_lowercase + ' a_'
    try:
        a = open(arquivo, 'at')
    except:
        print('falha ao registrar palavra')
    else:
        while True:
            word = input('Palavra: ').replace(' ', '_')
            if all(c in validos for c in word):
                if not verificarExistencia(word, arquivo):
                    a.write(f'{word}\n')
                    a.close()
                    break
                else:
                    print('palavra já registrada')
            else:
                print('palavra inválida')

#verifica se a palavra ja existe no arquivo
def verificarExistencia(palavra, arch):
    arch = open(arch, 'rt')
    lista = arch.readlines()
    for i, v in enumerate(lista):
        lista[i] = v.replace('\n', '')
    if palavra in lista:
        return True
    else:
        return False

#exclue uma palavra de um arquivo
def excluirPalavra(arquivo):
    validos = ascii_lowercase + ' a_'

    while True:
        word = input(
            f'{ciano}Palavra p/ excluir{original}: ').replace(' ', '_')

        if all(c in validos for c in word):
            if verificarExistencia(word, arquivo):
                try:
                    with open(arquivo, 'r') as a:
                        linhas = a.readlines()

                        with open(arquivo, 'w') as aw:
                            for linha in linhas:
                                if linha.strip('\n') != word:
                                    aw.write(linha)
                    print('excluído')
                    break
                except Exception as e:
                    print(f'erro {e}')
                else:
                    print()
            else:
                print('palavra não registrada')
        else:
            print('palavra inválida')

#cria cabeçalhos
def header(msg):
    print('-'*42)
    print(f'{msg}'.center(42))
    print('-'*42)

#cria uma lista com as palavras registradas
def palavrasRegistradas(arquivo):
    a = open(arquivo, 'rt')
    lista = a.readlines()
    palavras = list()

    header("PALAVRAS REGISTRDAS")
    for i, v in enumerate(lista):
        if ((i+1) % 2) == 0:
            p = v.replace('\n', '').replace('_', ' ')
            print(f'{vermelho}{p}{original}')
        else:
            p = v.replace('\n', '').replace('_', ' ')
            print(f'{ciano}{p}{original}')

    print('-'*42)
