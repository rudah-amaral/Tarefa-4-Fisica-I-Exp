import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set_theme(
  #palette = "Set2",
  font_scale = 0.9,
  rc = {
    "figure.figsize": (5, 4),
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
  },
)
sns.set_style("darkgrid")
mpl.use("pgf")

def gera_imagem(amostras, titulo, definicoes):
    x = amostras.x
    y = amostras.y

    # desvio_y = None
    if("desvio_y" in amostras.columns):
        desvio_y = amostras.desvio_y
    desvio_x = None
    if("desvio_x" in amostras.columns):
        desvio_x = amostras.desvio_x

    a = definicoes["a"]
    b = definicoes["b"]
    x_label = definicoes["x_label"]
    y_label = definicoes["y_label"]
    a_legend = definicoes["a_legend"]
    b_legend = definicoes["b_legend"]
    text_size = definicoes["text_size"]
    text_offset_x = definicoes["text_offset_x"]
    text_offset_y = definicoes["text_offset_y"]

    # n = len(amostras)
    # x = amostras.x
    # y = amostras.y

    # # Denominador comum
    # d = (n * (x ** 2).sum()) - (x.sum() ** 2)

    # a =  ( n * (x*y).sum() - x.sum()*y.sum()) / d
    # b = ((x ** 2).sum() * y.sum() - (x * y).sum() * x.sum()) / d

    # y_esperado = a*x + b
    # erro = (y_esperado - y)
    # sse = (erro ** 2).sum()
    # sigma2 = sse / (n - 2)

    # a_erro = math.sqrt((n * sigma2) / d)
    # b_erro = math.sqrt(((x ** 2).sum() * sigma2) / d)

    # print()
    # print("COEFICIENTES DA RETA DE REGRESSÃO")
    # print(f"Coeficiente a = {a} ± {a_erro}")
    # print(f"Coeficiente b = {b} ± {b_erro}")

    if(a or b):
        ssr = ((a*x + b - y.mean()) ** 2).sum()
        sst = ((y - y.mean()) ** 2).sum()

        r2 = ssr / sst

    if(
        "desvio_y" in locals() and
        a != None
        # "a" in locals() and
        # "b" in locals
    ):
        chi2 = (((y - b - a*x) / desvio_y) ** 2).sum()

    # print()
    # print("MÉTRICAS DA REGRESSÃO")
    # print(f"Coeficiente r² = {r2}")
    # print(f"Coeficiente χ² = {chi2}")
    # print(f"sst = \t\t{sst}")
    # print(f"ssr + sse = \t{ssr + sse}")

    # delta_x = amostras["delta_t (s)"]
    # precisao_x = (1 - abs(a_erro / a)) * 100
    # delta_y = amostras["delta_s (m)"]
    # precisao_y = (1 - abs(b_erro / b)) * 100
    #
    # print()
    # print("MÉTRICAS DA REGRESSÃO")
    # print(f"{precisao_x}")
    # print(f"{precisao_y}")

    amostras.sort_values(by = "x")
    fig, ax = plt.subplots()

    if(a or b):
        regressao_x = amostras["x"].iloc[[0, -1]]
        regressao_x.iloc[0] -= .01
        regressao_x.iloc[1] += .01
        regressao_y = regressao_x * a + b
        regressao = sns.lineplot(
        x = regressao_x,
        y = regressao_y,
        ax = ax,
        label = "Ajuste",
        color = "orange"
        )
    
    if("desvio_y" in locals()):
        ax.errorbar(
            x = amostras.x,
            y = amostras.y,
            yerr = desvio_y,
            fmt = "none",
            ecolor = "black",
            elinewidth = 1,
            capsize = 3,
        )

    experimental = sns.scatterplot(
        data = amostras,
        x = x,
        y = y,
        label = "Dados Experimentais"
    )

    #for i in range(len(amostras)):
    #    ax.text(
    #        x[i] + text_offset_x,
    #        y[i] + text_offset_y,
    #        f"({round(x[i], 2)}, {round(y[i], 2)})",
    #        ha = "left",
    #        va = "center",
    #        fontsize = text_size,
    #    )

    # Hack sujo pra adicionar legenda
    if(a_legend):
        plt.plot([], [], ' ', label = a_legend)
    if(b_legend):
        plt.plot([], [], ' ', label = b_legend)
    if("r2" in locals()):
        plt.plot([], [], ' ', label=f"$R^2 = {round(r2, 3)}$")
    if("chi2" in locals()):
        plt.plot([], [], ' ', label=f"$\chi^2 = {round(chi2, 3)}$")
    ax.legend()

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    fig.tight_layout()
    sns.despine()

    # Adiciona a sub-grade
    ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    ax.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
    ax.grid(which='minor', color='w', linewidth = 0.5)

    plt.savefig(f'imagens/{titulo}.png')
    plt.savefig(f'imagens/{titulo}.pgf')
