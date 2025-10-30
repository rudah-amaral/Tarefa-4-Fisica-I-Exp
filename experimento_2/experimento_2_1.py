import numpy as np
import pandas as pd
import calcula_grafo

col_names = ["y", "x"]
amostras = pd.read_csv(
    "experimento_2/dados.dat",
    sep = "\t",
    header = None,
    skiprows = [0, 1],
    names = col_names,
)

definicoes = {
    "a": None,
    "b": None,
    "x_label": "R (u.a.)",
    "y_label": "T (anos)",
    "a_legend": None,
    "b_legend": None,
    "text_size" : 6,
    "text_offset_x" : 0,
    "text_offset_y" : -5,
}

calcula_grafo.gera_imagem(amostras, "exercicio 2.1", definicoes)

# Gera amostras aleatórias com um pouco de barulho. Saberemos que a regresão
# estará correta se retornar a mesma reta que gerou esse valores.
#def gera_amostras(qntd_amostras, intensidade_barulho):
#    coeficiente_angular = 1
#    coeficiente_linear = 0
#
#    max = intensidade_barulho
#    min = -intensidade_barulho
#    barulho = (max - min) * np.random.random_sample(qntd_amostras) + min
#
#    base_amostras = np.array(range(1,11))
#    amostras = pd.DataFrame({
#        "x": base_amostras,
#        "y": base_amostras * coeficiente_angular + coeficiente_linear + barulho,
#        "desvio_y": intensidade_barulho
#    })
#
#    return amostras
