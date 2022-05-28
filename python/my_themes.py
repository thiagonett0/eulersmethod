"""
Descrição: código que determina as cores usadas nos gráficos e possui os templates aplicados.
"""


import plotly.graph_objects as go
import plotly.io as pio
import numpy as np


pio.templates["draft"] = go.layout.Template(
        layout_annotations=[
            dict(
                name="draft watermark",
                text=" ",
                textangle=0,
                opacity=0.1,
                font=dict(color="black", size=100),
                xref="paper",
                yref="paper",
                x=0.5,
                y=1,
                showarrow=False,
            )
        ]
    )


pio.templates["middle"] = go.layout.Template(
        layout_annotations=[
            dict(
                name="draft watermark",
                text=" ",
                textangle=0,
                opacity=0.1,
                font=dict(color="black", size=100),
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                showarrow=False,
            )
        ]
    )


def paletteGenerator(number):

    """
    Descrição: executa a escolha aleatória de cores das seguintes paletas abaixo. Para tal,
                recebe-se a entrada number que determina qual das paletas será a escolhida.
                Por fim, já 'dentro' da paleta, determina novamente aleatoriamente qual das
                cores utilizar;
    
    Entrada(s):
                i) number (int): inteiro que determina qual paleta usar;

    Saída(s):
                i) color (str): nome da cor escolhida.
    """

    paletteDict = {
        # palette name : [colors in HEX]
        'viridis': [
            '#00725c', '#007a63', '#008269', '#008a70', '#009277', '#009b7d',
            '#00a384', '#00ab8a', '#00b391', '#00bb98', '#00c39e', '#00cca5'
        ],
        'carolina-blue': [
            '#002572', '#00287a', '#002b82', '#002d8a', '#003092', '#00339b',
            '#0035a3', '#0038ab', '#003bb3', '#003ebb', '#0040c3', '#0043cc'
        ],
        'chestnut-leather': [
            '#dd9789', '#df9c8f', '#e1a296', '#e3a79c', '#e4ada2', '#e6b3a9',
            '#e8b8af', '#eabeb5', '#ecc4bc', '#edc9c2', '#efcfc8', '#f1d4cf'
        ],
        'colorscale0': ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", 
            "#b3d2e9", "#9ecae1", "#85bcdb", "#6baed6", "#57a0ce", "#4292c6",
            "#3082be", "#2171b5", "#1361a9", "#08519c", "#0b4083", "#08306b"]
    }
    palette = list(paletteDict.keys())[number%len(paletteDict)]
    color = paletteDict[palette][np.random.randint(0, len(paletteDict[palette]))]
    return color


def paletteGenerator2(number):

    """
    Descrição: semelhante à anterior. Porém, em vez de retornar apenas uma das cores da paleta,
                retorna a paleta toda no formato de lista;
    
    Entrada(s):
                i) number (int): idem à anterior;
        
    Saída(s):
                i) paletteDict[palette] (list): paleta escolhida.
    """

    paletteDict = {
        # palette name : [colors in HEX]
        'viridis': [
            '#00725c', '#007a63', '#008269', '#008a70', '#009277', '#009b7d',
            '#00a384', '#00ab8a', '#00b391', '#00bb98', '#00c39e', '#00cca5'
        ],
        'carolina-blue': [
            '#002572', '#00287a', '#002b82', '#002d8a', '#003092', '#00339b',
            '#0035a3', '#0038ab', '#003bb3', '#003ebb', '#0040c3', '#0043cc'
        ],
        'chestnut-leather': [
            '#dd9789', '#df9c8f', '#e1a296', '#e3a79c', '#e4ada2', '#e6b3a9',
            '#e8b8af', '#eabeb5', '#ecc4bc', '#edc9c2', '#efcfc8', '#f1d4cf'
        ],
        'colorscale0': ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", 
            "#b3d2e9", "#9ecae1", "#85bcdb", "#6baed6", "#57a0ce", "#4292c6",
            "#3082be", "#2171b5", "#1361a9", "#08519c", "#0b4083", "#08306b"]
    }
    palette = list(paletteDict.keys())[number%len(paletteDict)]
    return paletteDict[palette]
