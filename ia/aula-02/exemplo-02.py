import numpy as np


_entradas = np.array([1,0])
_pesos = np.array([0.3, -0.1])


def soma(entrada, peso):
    return entrada.dot(peso)


s = soma(_entradas, _pesos)
print(s)


def fdegrau(soma):
    if (soma >= 0.1):
        return 1
    return 0


r = fdegrau(s)
print(r)
