"""
Descrição: código que executa a construção dos gráficos das soluções.
"""


import numpy as np

import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

import my_themes


def grafico(funcoes):

    """
    Descrição: executa a construção do gráfico das soluções. Para tal, faz-se uso do template middle do arquivo my_themes. 
                Após isso, constrói-se como usualmente se faz por meio da biblioteca Plotly. Perceba que itera-se sob as
                soluções, que vão da segunda linha da matriz em diante, já que a primeira determina o domínio da variável
                independente. Por fim, nomeia-se os eixos e o gráfico;
        
    Entrada(s):
                i) funcoes (list): matriz que contém as funções que satisfazem o sistema;
    
    Saída(s):
                i) None.
    """

    pio.templates.default = "middle"
    color = np.random.randint(5)
    fig = make_subplots(
                rows=1, cols=1,
                specs=[[{}]],
                subplot_titles=())
    for indice, funcao in enumerate(funcoes[1:], 1):
        fig.add_trace(go.Scatter(x = funcoes[0], y = funcao, mode='lines', name = indice, line=dict(color=my_themes.paletteGenerator(np.random.randint(5)))), row=1, col=1)
    fig.update_xaxes(title_text='t (s)', row=1, col=1)
    fig.update_yaxes(title_text='f(t) (SI)', row=1, col=1)
    fig.update_layout(title_text="Curva da corrente e tensão do circuito",
                  title_font_size=20)
    fig.show()
    return None
