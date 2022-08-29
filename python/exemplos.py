"""
Descrição: código que soluciona os exemplos discutidos no arquivo de apresentação do repositório (readme.md).
"""


import numpy as np
from euler import metodoEuler
from eulerNewton import eulerNewton


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


# metodoEuler(1e-3, 1e-1, [0, 0], rlcNulo, "Curva da corrente e tensão do circuito", ['Corrente', 'Tensão'])


# Solução do pêndulo esférico de comprimento 0.10 m:


def pendEsferico(t, y0):

    """
    Descrição: função que determina o vetor de equações a serem resolvidas
                pelo método de Euler. Adicionalmente, define-se os parâmetros
                todos em conformidade com o Sistema Internacional (SI);

    Entrada(s): idem função equacoes do arquivo euler. Nesse caso, y0 = [argX, argZ, velX = z0, velZ = z1];

    Saída(s): idem função equacoes do arquivo euler.
    """

    g, l = 9.81, 0.10
    vetor = [
        y0[2],
        y0[3],
        -2*(np.cos(y0[1])/np.sin(y0[1]))*y0[2]*y0[3],
        (y0[2]**2)*np.sin(y0[1])*np.cos(y0[1]) - (g/l)*np.sin(y0[1])
    ]
    return vetor


#metodoEuler(1e-6, 1, [0, 1.57, 0.1, 0], pendEsferico, f"Curvas do movimento do pêndulo esférico", ['Posição, arg(X)', 'Posição, arg(Z)', 'Velocidade, arg(X)', 'Velocidade, arg(Z)'])


# Solução do pêndulo esférico de comprimento 0.10 m:


def degrauUnit(x):
    if x >= 0:
        return 1
    else:
        return 0


def pendEsferico2(t, y0):

    """
    Descrição: função que determina o vetor de equações a serem resolvidas
                pelo método de Euler. Adicionalmente, define-se os parâmetros
                todos em conformidade com o Sistema Internacional (SI);

    Entrada(s): idem função equacoes do arquivo euler. Nesse caso, y0 = [argX, argZ, velX = z0, velZ = z1];

    Saída(s): idem função equacoes do arquivo euler.
    """

    m, g, l, k, n = 100, 9.81, 0.10, 10000000, 10
    vetor = [
        y0[2],
        y0[3],
        -y0[2]*(2*(np.cos(y0[1])/np.sin(y0[1]))*y0[3] + (k*l/m)*degrauUnit(y0[1]-np.arccos(1/n))*np.sqrt(y0[3]**2 + np.sin(y0[1])*y0[2]**2)),
        (y0[2]**2)*np.sin(y0[1])*np.cos(y0[1]) - (g/l)*np.sin(y0[1]) - (k*l/m)*degrauUnit(y0[1]-np.arccos(1/n))*np.sqrt(y0[3]**2 + np.sin(y0[1])*y0[2]**2)*y0[3]
    ]
    return vetor


# metodoEuler(1e-5, 2, [0, 1.57, 0, 0], pendEsferico2, f"Curvas do movimento do pêndulo esférico", ['Posição, arg(X)', 'Posição, arg(Z)', 'Velocidade, arg(X)', 'Velocidade, arg(Z)'])


# Solução de um circuito RLC estocástico em série com condições iniciais nulas (por Euler Implícito)


from math import cos, sin
from random import gauss


def g1(x):
    return 1


def g2(x):
    return x[0]


def g3(x):
    return x[1]


def matrizCoeficientes(t):
    # R, L, C, V = 5 + gauss(0, 2), 10e-3 + gauss(0, 1e-7), 183e-6 + gauss(0, 1e-7), gauss(5*sin(t), 0.5)
    R, L, C, V = 10 + gauss(0, 2), 20e-3 + gauss(0, 1e-7), 5e-3 + gauss(0, 1e-7), gauss(1, 0.25)
    m = [[V/L, -R/L, -1/L], [0, 1/C, 0]]
    return m


s = eulerNewton(matrizCoeficientes, [g1, g2, g3], 1e-4, [0, 0], 10, 'Circuito RLC Estocástico', ['I', 'Vcapacitor'])


# Solução de um pêndulo tridimensional (Euler Implícito por Newton)


def g1(x): return cos(x[3])*x[0]*x[1]/sin(x[3])


def g2(x): return (x[0]**2)*sin(x[3])*cos(x[3])


def g3(x): return sin(x[3])


def g4(x): return x[0]


def g5(x): return x[1]


def matrizCoeficientes(t):
    g, l = 9.8, 0.1
    m = [[-2, 0, 0, 0, 0], [0, 1, -g/l, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    return m


# s = eulerNewton(matrizCoeficientes, [g1, g2, g3, g4, g5], 1e-4, [0.2, 0.01, 0, 1.57], 10, 'Pêndulo 3D', ['Vel phi', 'Vel theta', 'Phi', 'Theta'])


def g1(x): return x[0]


def g2(x): return x[0]*x[1]


def g3(x): return x[1]


def matrizCoeficientes(t):

    """
    Descrição: matriz coeficientes para o sistema presa-predador. As constantes seguem-se conforme:
                
                i) a (float): proporcionalidade para taxa de reprodução das presas (sucesso de reprodução);
                ii) b (float): proporcionalidade para taxa de mortes das presas (chance de ser devorado);
                iii) c (float): proporcionalidade para a taxa de morte dos predadores (morte por fome);
                iv) d (float): proporcionalidade para a taxa de reprodução dos predadores (sucesso em predação);

    Entrada(s):
                i) t (float): variável tempo;
    
    Saída(s):
                i) m (list): matriz coeficientes.
    """

    a, b, c, d = 0.2*(sin(t) + 0.5*sin(3*t) + 0.2*sin(11*t) + gauss(3, 1)), 0.02, 0.4, 0.03*(sin(2*t) + 0.01*sin(3*t) + 0.0005*sin(23*t) + gauss(1.5, 0.1))
    m = [[a, -b, 0], [0, d, -c]]
    return m


# s = eulerNewton(matrizCoeficientes, [g1, g2, g3], 1e-2, [10, 50], 50, 'Lotka-Volterra', ['Presa', 'Predador'])

# https://mbe.modelica.university/behavior/equations/population/


# Reação química sei lá o que

def g1(x): return x[0]


def g2(x): return x[1]*x[2]


def g3(x): return x[1]**2


def matrizCoeficientes(t):

    """
    Descrição: ...;

    Entrada(s):
                i) t (float): variável tempo;
    
    Saída(s):
                i) m (list): matriz coeficientes.
    """

    m = [[-4e-2, 1e4, 0], [4e-2, -1e4, -3e7], [0, 0, 3e7]]
    return m


# s = eulerNewton(matrizCoeficientes, [g1, g2, g3], 1e-2, [1, 0, 0], 300, 'Robertsons autocatalytic chemical reaction', ['[X]', '[Y]', '[Z]'])

# https://scipython.com/book2/chapter-8-scipy/examples/solving-a-system-of-stiff-odes/

