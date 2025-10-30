import numpy as np
import pandas as pd
import calcula_grafo

col_names = ["y", "desvio_y", "x", "desvio_x"]
amostras = pd.read_csv(
    "experimento_3/dados.dat",
    sep = "\t",
    header = None,
    skiprows = [0, 1],
    names = col_names,
    skipfooter = 3, 
    engine= "python"
)

# amostras.y = amostras.y ** 2
# amostras.x = amostras.x ** 3

definicoes = {
    "a": None,
    "b": None,
    "x_label": "m (g)",
    "y_label": "10T (s)",
    "a_legend": None,
    "b_legend": None,
    "text_size" : 6,
    "text_offset_x" : 5,
    "text_offset_y" : -1,
}

# print(amostras)
calcula_grafo.gera_imagem(amostras, "exercicio 3.1", definicoes)

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
