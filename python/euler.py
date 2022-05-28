"""
Descrição: código que executa soluções de sistemas de equações diferenciais por meio do método de Euler. Ao final,
            faz-se uso de outro código (graphs) para graficar as soluções.
"""


from graficos import *


def soma(i, j):

    """
    Descrição: opera a soma entre dois números reais;

    Entrada(s):
                i) i (float): número real;
                ii) j (float): número real;
    
    Saída(s):
                i) i + j (float): resultado da operação.
    """

    return i+j


def subtracao(i, j):

    """
    Descrição: análogo à função anterior;

    Entrada(s): análogo à função anterior;
    
    Saída(s): análogo à função anterior.
    """

    return i-j


def somaVetorial(u, v, operacao):

    """
    Descrição: opera soma entre dois vetores reais. Nesse caso, a validação da operação se dá por meio de exceção;

    Entrada(s):
                i) u (list): vetor real;
                ii) v (list): vetor real;
                iii) operacao (func): função de operação entre os elementos dos vetores;

    Saída(s):
                i) s (list): resultado da operação;
                ii) None.
    """

    try:
        s = list()
        for i, j in zip(u, v):
            s.append(operacao(i, j))
        return s
    except IndexError:
        print(f"Os vetores têm que possuir mesma dimensão!")
        return None


def somaVetorial2(u, v, operacao):

    """
    Descrição: opera soma entre dois vetores reais. Nesse caso, a validação da operação se dá por meio de uma cláusula if;

    Entrada(s):
                i) u (list): vetor real;
                ii) v (list): vetor real;
                iii) operacao (func): função de operação entre os elementos dos vetores;

    Saída(s):
                i) s (list): resultado da operação;
                ii) None.
    """

    if len(u) == len(v):
        s = list()
        for i, j in zip(u, v):
            s.append(operacao(i, j))
        return s
    else:
        print(f"Os vetores têm que possuir mesma dimensão!")
        return None


def produtoEscalar(a, u):

    """
    Descrição: opera o produto escalar;

    Entrada(s):
                i) a (float): número real a escalar o vetor;
                ii) u (list): vetor a ser escalado;
    
    Saída(s):
                i) u (list): vetor já escalado.
    """

    for indice, i in enumerate(u, 0):
        u[indice] = a*i
    return u


def equacoes(t, y0):

    """
    Descrição: vetor que dispõe as equacões escalares, denominadas usualmente por f, para execução do método de Euler;

    Entrada(s):
                i) t (float): variável independente;
                ii) y0 (list): vetor de entrada no passo anterior;

    Saída(s):
                i) vetor (list): equações avaliadas no passo anterior.
    """
    
    vetor = [
        # equação 1,
        # equação 2,
        # ...  ...,
        # equação n,
    ]
    return vetor


def metodoEuler(h, limite, y0, equacoes):

    """
    Descrição: executa o método de Euler para um sistema de equações diferenciais lineares de primeira ordem. Ao executar
                o método no i-ésimo passo, salva todas as informações em solucaoNum. Ao final, por conveniência, calcula
                sua transposta por meio de np.transpose da biblioteca numpy;

    Entrada(s):
                i) h (float): passo;
                ii) limite (float): limite para a variável independente;
                iii) y0 (list): vetor de condição inicial;
                iv) equacoes (func): vetor de equações a serem resolvidas;
    
    Saída(s):
                i) solucaoNum (list): matrix contendo a variável independente e as soluções numéricas dispostas por linhas.
    """

    t = h
    solucaoNum = list()
    while t <= limite:
        y = somaVetorial(y0, produtoEscalar(h, equacoes(t, y0)), soma)
        solucaoNum.append([t] + y)
        t += h
        y0 = y
    solucaoNum = np.transpose(solucaoNum)
    grafico(solucaoNum)
    # print(solucaoNum)
    return solucaoNum
