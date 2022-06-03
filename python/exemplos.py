"""
Descrição: código que soluciona os exemplos discutidos no arquivo de apresentação do repositório (readme.md).
"""


import numpy as np
from euler import metodoEuler


# Solução de um circuito RLC em série com condições iniciais nulas:


def rlcNulo(t, y0):
    
    """
    Descrição: função que determina o vetor de equações a serem resolvidas
                pelo método de Euler. Adicionalmente, define-se os parâmetros
                todos em conformidade com o Sistema Internacional (SI);

    Entrada(s): idem função equacoes do arquivo euler;

    Saída(s): idem função equacoes do arquivo euler.
    """
    
    R, L, C, V = (1.6 + 8.2/3), 10e-3, 183e-6, 5
    vetor = [
        (V-y0[0]*R-y0[1])/L,
        y0[0]/C
    ]
    return vetor


metodoEuler(1e-6, 1e-1, [0, 0], rlcNulo, "Curva da corrente e tensão do circuito", ['Corrente', 'Tensão'])


# Solução do pêndulo esférico de comprimento 0.10 m:


def pendEsferico(t, y0):

    """
    Descrição: função que determina o vetor de equações a serem resolvidas
                pelo método de Euler. Adicionalmente, define-se os parâmetros
                todos em conformidade com o Sistema Internacional (SI);

    Entrada(s): idem função equacoes do arquivo euler. Nesse caso, y0 = [argX, argZ, z0, z1];

    Saída(s): idem função equacoes do arquivo euler.
    """

    g, l = 9.81, 0.10
    vetor = [
        y0[2],
        y0[3],
        -2*(np.cos(y0[1])/np.sin(y0[1]))*y0[2]*y0[3],
        y0[2]*np.sin(y0[1])*np.cos(y0[1]) - (g/l)*np.sin(y0[1])
    ]
    return vetor


# metodoEuler(1e-5, 2, [0, 1.57, 0, 0], pendEsferico, f"Curvas do movimento do pêndulo esférico", ['Posição, arg(X)', 'Posição, arg(Z)', 'Velocidade, arg(X)', 'Velocidade, arg(Z)'])
