"""
Descrição: código que executa soluções de sistemas de equações diferenciais por meio do método de Euler implícito.
            Ao final, faz-se uso de outro código (graphs) para graficar as soluções.
"""

import sys
sys.path.append( 'path' )
sys.path.append( 'path' )

import linalg as la
import calculus as cs
import ludecomposition as lu
from graficos import *


def evaluateG(vectorG, x0):

    """
    Descrição: calcula a função vetorial vectorG em x0;

    Entrada(s):
                i) vectorF (list): função vetorial G;
                ii) x0 (list): ponto a avaliar G;
    
    Saída(s):
                i) x (list): função no vetor entrada.
    """

    x = list()
    for i in vectorG:
        x.append(i(x0))
    return x


def eulerNewton(matrizCoeficientes, vetorG, h, estimativa0, T, titulo, quantidades):

    """
    Descrição: seja F uma função vetorial diferenciável tal que F = 0. Então, calcula-se suas raízes numericamente por meio do
                Método de Newton;

    Entrada(s):
                i) ...
    
    Saída(s):
                i) ...
    """

    x0 = estimativa0
    dimDomain = len(x0)
    dimRange = len(vetorG)
    t = 0
    solucao = list()
    while t < T:
        I = la.identityMatrix(dimDomain)
        J = la.matrixProduct(matrizCoeficientes(t), cs.jacobian(vetorG, dimDomain, dimRange, x0, 1e-6))
        A = la.matrixSum(I, la.matrixScalar(-h, J))
        b = la.vectorScalar(h, la.matrixVector(matrizCoeficientes(t), evaluateG(vetorG, x0)))
        z = lu.solucaoLU(A, b)
        x = la.vectorSum(z, x0)
        solucao.append([t] + x)
        x0 = x
        t += h
    solucao = la.matrixTranspose(solucao)
    grafico(solucao, titulo, f'Sujeito a y0 = {estimativa0} (SI)', quantidades)
    return solucao
