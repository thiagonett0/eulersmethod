"""
Descrição: código que executa soluções de sistemas de equações diferenciais por meio do método de Euler. Ao final,
            faz-se uso de outro código (graphs) para graficar as soluções.
"""


import sys
sys.path.append( 'path' )

import linalg as la
from graficos import *


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


def metodoEuler(h, limite, y0, equacoes, titulo, quantidades):

    """
    Descrição: executa o método de Euler para um sistema de equações diferenciais lineares de primeira ordem. Ao executar
                o método no i-ésimo passo, salva todas as informações em solucaoNum. Ao final, por conveniência, calcula
                sua transposta por meio de np.transpose da biblioteca numpy;

    Entrada(s):
                i) h (float): passo;
                ii) limite (float): limite para a variável independente;
                iii) y0 (list): vetor de condição inicial;
                iv) equacoes (func): vetor de equações a serem resolvidas;
                v) titulo (str): título do gráfico;
                vi) quantidades (list): lista com nomes das quantidades a serem resolvidas;
    
    Saída(s):
                i) solucaoNum (list): matrix contendo a variável independente e as soluções numéricas dispostas por linhas.
    """

    t = h
    solucaoNum, condInicial = list(), y0
    while t <= limite:
        y = la.vectorSum(y0, la.dotProduct(h, equacoes(t, y0)))
        solucaoNum.append([t] + y)
        t += h
        y0 = y
    solucaoNum = la.matrixTranspose(solucaoNum)
    grafico(solucaoNum, titulo, f'Sujeito a y0 = {condInicial} (SI)', quantidades)
    # print(solucaoNum)
    return solucaoNum
