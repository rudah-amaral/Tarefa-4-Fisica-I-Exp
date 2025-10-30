import numpy as np
import pandas as pd
import calcula_grafo

col_names = ["y", "desvio_y", "x", "desvio_x"]
amostras = pd.read_csv(
    "experimento_1/dados.dat",
    sep = "\t",
    header = None,
    skiprows = [0],
    names = col_names,
    skipfooter = 3, 
    engine= "python"
)

definicoes = {
    "a": 36.7985,
    "b": -310,
    "x_label": "t (s)",
    "y_label": "s (mm)",
    "a_legend": "$v = 0,0367986 \\pm 0,0001155$",
    "b_legend": "$s_0 = -0,0310 \\pm 0,03584$",
    "text_size" : 6,
    "text_offset_x" : 5,
    "text_offset_y" : -500,
}

calcula_grafo.gera_imagem(amostras, "exercicio 1", definicoes)

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
