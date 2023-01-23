import math

destino = ['Afeganistão',
           'Argélia',
           'Brasil',
           'Canadá',
           'França',
           'Gana',
           'Hungria',
           'Indonesia',
           'Japão',
           'Líbano',
           'Malásia',
           'Marrocos',
           'México',
           'Nepal',
           'Paquistão',
           'Peru',
           'Portugal',
           'Quênia',
           'Romenia',
           'Ruanda',
           'Samoa',
           'Singapura',
           'Tunisia',
           'Uruguai',
           'Zimbabue',
           'Dummy']

origem = ['Brasil',
          'Canadá',
          'França',
          'Japão',
          'Singapura',
          'Zimbabue']

custos = [
    [6.69, 9.55, 0.00, 8.28, 5.10, 5.41, 5.73, 7.96, 7.64, 8.92, 4.78, 5.10, 3.82,
        8.28, 8.60, 8.92, 3.50, 4.78, 6.69, 4.78, 4.14, 3.18, 4.14, 6.37, 4.46, 999],
    [8.92, 5.41, 3.50, 0.00, 8.60, 7.64, 4.14, 7.96, 8.92, 9.55, 5.73, 7.96, 5.73,
        8.60, 9.55, 4.14, 4.14, 7.01, 7.96, 6.69, 3.50, 7.96, 4.14, 7.32, 7.01, 999],
    [5.73, 6.05, 6.69, 3.50, 0.00, 3.50, 7.01, 8.92, 4.14, 9.55, 8.28, 6.05, 8.28,
        8.60, 9.24, 8.28, 3.18, 4.78, 5.73, 8.92, 5.41, 7.64, 6.69, 4.14, 5.41, 999],
    [6.05, 6.69, 3.18, 7.01, 6.37, 9.55, 5.73, 6.37, 0.00, 6.05, 8.60, 7.32, 7.96,
        3.50, 6.37, 9.24, 3.18, 3.18, 4.14, 4.14, 6.05, 5.10, 4.46, 9.55, 7.32, 999],
    [5.41, 4.46, 6.05, 9.55, 4.78, 8.92, 5.10, 8.60, 4.14, 8.92, 4.14, 4.78, 4.14,
        6.37, 3.18, 3.50, 6.05, 5.10, 5.73, 3.50, 7.64, 0.00, 6.69, 4.78, 4.78, 999],
    [7.96, 3.82, 5.41, 9.55, 6.69, 9.24, 7.96, 6.37, 7.96, 3.50, 8.28, 5.73, 9.55,
        5.73, 9.24, 5.73, 6.05, 8.60, 7.64, 3.18, 7.64, 6.37, 7.96, 9.55, 0.00, 999]

]


disponibilidade = [7500, 8100, 4900, 5300, 3900, 3600]

necessidade = [1673, 963, 1444, 1282, 2193, 782, 683, 906, 1195, 962, 1782, 1147,
               1711, 1441, 1878, 1172, 1254, 548, 643, 1986, 929, 2173, 1907, 1908, 666, 72]


resultado_custos = []


def inicia_resultado_custos():
    coluna = []
    for i in range(0, len(custos)):
        for j in range(0, len(custos[0])):
            coluna.append(0)
        resultado_custos.append(coluna.copy())
        coluna.clear()


def soma_sem_nulo(lista):
    resultado = 0
    for num in lista:
        if num is not None:
            resultado += num
    return resultado


def calcula_penalidades():
    penalidade_origem = []
    penalidade_destino = []
    aux = []

    for i, linha in enumerate(custos):
        penalidade_origem.append(diferenca_menor_custo(
            lista_sem_nulo(linha, necessidade)))

    for j in range(0, len(custos[0])):
        for k in range(0, len(custos)):
            aux.append(custos[k][j])
        penalidade_destino.append(diferenca_menor_custo(
            lista_sem_nulo(aux, disponibilidade)))
        aux.clear()

    return [penalidade_origem, penalidade_destino]


def diferenca_menor_custo(lista):

    menor = min(lista)
    lista.remove(menor)

    if len(lista) == 0:
        return menor

    segundo_menor = min(lista)

    return segundo_menor - menor


def get_coluna(index):
    coluna = []
    for j in range(0, len(custos)):
        coluna.append(custos[j][index])
    return coluna


def lista_sem_nulo(lista, lista_comparacao=None):
    remove_nulo_lista = []
    for i, x in enumerate(lista):
        if lista_comparacao is not None:
            if lista_comparacao[i] is not None:
                remove_nulo_lista.append(x)
        else:
            if lista[i] is not None:
                remove_nulo_lista.append(x)
    return remove_nulo_lista


def min_positivo(lista):
    for i, num in enumerate(lista):
        if num < 0:
            lista[i] = math.inf

    try:
        if min(lista) != math.inf:
            return min(lista)
        else:
            raise Exception('')
    except:
        exit(1)


def encontra_menor_celula(penalidade_origem, penalidade_destino):
    resultado = []

    maior_penalidade_origem = max(penalidade_origem)
    maior_penalidade_destino = max(penalidade_destino)

    if  maior_penalidade_destino > maior_penalidade_origem:
        index_maior_diferenca = penalidade_destino.index(
            maior_penalidade_destino)
        resultado.append(index_maior_diferenca)
        coluna = get_coluna(index_maior_diferenca)
        menor_valor_custo = min_positivo(
            lista_sem_nulo(coluna, disponibilidade))
        resultado.append(menor_valor_custo)
        resultado.append(coluna.index(menor_valor_custo))
    else:
        index_maior_diferenca = penalidade_origem.index(
            maior_penalidade_origem)
        resultado.append(index_maior_diferenca)
        linha = custos[index_maior_diferenca]
        menor_valor_custo = min_positivo(lista_sem_nulo(linha, necessidade))
        resultado.append(menor_valor_custo)
        resultado.append(linha.index(menor_valor_custo))
        resultado.reverse()

    return resultado


def calcula_resultado():
    z = 0
    for i in range(0, len(resultado_custos)):
        for j in range(0, len(resultado_custos[0])):
            if destino[j] == 'Dummy':
                    break
            z += resultado_custos[i][j]
    return z


def valor_transporte_individual():
    aux = 0
    dummy = 0
    resto = ''
    for i in range(0, len(resultado_custos)):
        for j, num in enumerate(resultado_custos[aux]):
            if num != 0:
                if destino[j] == 'Dummy':
                    resto = origem[i]
                    dummy = num 
                    break
                a = origem[i]
                b = destino[j]
                print(str(a)+" --> "+str(b)+" = " + str(num))
        aux = aux+1
    print("Dummy("+resto+"): "+str(dummy))


def main():

    inicia_resultado_custos()

    while (soma_sem_nulo(disponibilidade) + soma_sem_nulo(necessidade)) != 0:

        penalidade_origem, penalidade_destino = calcula_penalidades()
        index_coluna_necessidade, menor_valor_custo, index_linha_disponibilidade = encontra_menor_celula(
            penalidade_origem, penalidade_destino)

        valor_disponibilidade = disponibilidade[index_linha_disponibilidade]
        valor_necessidade = necessidade[index_coluna_necessidade]

        if  valor_disponibilidade > valor_necessidade:
            resultado_custos[index_linha_disponibilidade][index_coluna_necessidade] = menor_valor_custo * valor_necessidade
            for i in range(0, len(custos)):
                custos[i][index_coluna_necessidade] = -1
            necessidade[index_coluna_necessidade] = None
            disponibilidade[index_linha_disponibilidade] -= valor_necessidade
        else:
            resultado_custos[index_linha_disponibilidade][index_coluna_necessidade] = menor_valor_custo * valor_disponibilidade
            for i in range(0, len(custos[0])):
                custos[index_linha_disponibilidade][i] = -1
            disponibilidade[index_linha_disponibilidade] = None
            necessidade[index_coluna_necessidade] -= valor_disponibilidade


main()
print(resultado_custos)
print('===================================')
print('Transportes:')
valor_transporte_individual()
print('===================================')
print(calcula_resultado())
