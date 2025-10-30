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

amostras.y = amostras.y ** 2
amostras.x = amostras.x ** 3

definicoes = {
    "a": 1.00149,
    "b": 0,
    "x_label": "$R^3 (u.a.^3)$",
    "y_label": "$T^2 (anos^2)$",
    "a_legend": "$K = 1,001 \\pm 0,001 $",
    "b_legend": "$b = 0$",
    "text_size" : 6,
    "text_offset_x" : 5,
    "text_offset_y" : -500,
}

calcula_grafo.gera_imagem(amostras, "exercicio 2.2", definicoes)

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
