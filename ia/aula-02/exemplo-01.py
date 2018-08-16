_entradas = [0,0]
_pesos = [0.3, -0.1]


def soma(entrada, peso):
    s = 0
    for i in range(2):
        print(f'Entrada: #{_entradas[i]} Peso #{_pesos[i]}')
        s += entrada[i] * peso[i]

    return s


s = soma(_entradas, _pesos)


def fdegrau(soma):
    if (soma >= 0.1):
        return 1
    return 2
