import numpy as np
import math


_entradas = np.array(
    [
        [0, 0],
        [0, 1],
        [1,0],
        [1,1]
    ]
)

_pesos_camada_1 = np.array(
    [
        [-0.424, 0.358],
        [-0.74, -0.577],
        [-0.961, -0.469],
    ]
)

_saida = np.array([0, 1, 1, 0])


def ativacao(x):
    """
    Função de de ativação segmode
    :param x:
    :return:
    """
    y = 1 / (1 + math.exp(-x))

    # arredondar para 3 casas decimais
    y = round(y, 3)
    return y


def soma_camada_1(entradas, pesos):
    """
    Soma da camada camada 1

    :param entradas:
    :param pesos:
    :return:
    """
    resultado_intermediario = []
    for i in range(len(entradas)):
        x1, x2 = entradas[i]
        for j in range(len(pesos)):
            peso_x1, peso_x2 = pesos[j]
            resultado_intermediario.append(x1 * peso_x1 + x2 * peso_x2)

    return resultado_intermediario


resultado_somas_camada_1 = soma_camada_1(_entradas, _pesos_camada_1)
print('Resultado da soma da camada 1')
print(np.array(resultado_somas_camada_1).reshape(4, 3))
print('-' * 30)

resultado_ativacao = []

for resultado_soma in resultado_somas_camada_1:
    resultado_ativacao.append(ativacao(resultado_soma))

print('Resultado da função de ativação da camada 1')
print(np.array(resultado_ativacao).reshape(4,3))
print('-' * 30)

"""
    Gerando as novas entradas
    Foi necessário converter a lista para array
    o método reshape serve para colocar em matriz bi-direcional
"""
_novas_entradas = np.array(resultado_ativacao).reshape(4, 3)
_pesos_camada_2 = np.array([-0.017, -0.893, 0.148])

print('Novas entradas')
print(_novas_entradas)
print('-' * 30)

def soma_camada_2(entradas, pesos):
    """
    Soma da camada camada 2

    :param entradas:
    :param pesos:
    :return:
    """
    resultado_intermediario = []
    for i in range(len(entradas)):
        x1, x2, x3 = entradas[i]
        peso_x1, peso_x2, peso_x3 = pesos
        somatorio = x1 * peso_x1 + x2 * peso_x2 + x3 * peso_x3
        resultado_intermediario.append(round(somatorio, 3))

    return resultado_intermediario


print('Resultado soma camada 2')
resultado_somas_camada_2 = soma_camada_2(_novas_entradas, _pesos_camada_2)
print(soma_camada_2(_novas_entradas, _pesos_camada_2))
# Aqui tem uma pequena diferença no segundo resultado
print('-' * 30)

print('Resultado da ativação')
resultado_ativacao = []
for resultado_soma in resultado_somas_camada_2:
    resultado_ativacao.append(ativacao(resultado_soma))

print(resultado_ativacao)