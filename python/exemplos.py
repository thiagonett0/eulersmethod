"""
Descrição: código que soluciona os exemplos discutidos no arquivo de apresentação do repositório (readme.md).
"""

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


metodoEuler(1e-6, 1e-1, [0, 0], rlcNulo)
