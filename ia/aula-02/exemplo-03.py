import numpy as np

_entradas = np.array([[0, 0], [0,1], [1,0], [1,1]])
_saidas = np.array([0,0,0,1])
_pesos = np.array([0.3, -0.1])
_taxa_aprendizagem = 0.1


def limit(soma):
    if soma >= 1:
        return 1
    return 0


def calcula_saida(registro):
    s = registro.dot(_pesos)
    return limit(s)


def treinar():
    erro_total = 1
    while erro_total != 0:
        erro_total = 0
        for i in range(len(_saidas)):
            saida_calculada = calcula_saida(np.asarray(_entradas[i]))
            erro = _saidas[i] - saida_calculada
            erro_total += erro
            for j in range(len(_pesos)):
                _pesos[j] = _pesos[j] + (_taxa_aprendizagem * _entradas[i][j] * erro)
                print(f'Pesos atualizados #{_pesos[j]}')
        print(f'Total erros #{erro_total}')


treinar()
print('Rede neural treinada')

for item in _entradas:
    print(calcula_saida(item))
