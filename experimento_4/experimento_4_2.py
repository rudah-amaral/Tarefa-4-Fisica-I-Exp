import calcula_grafo
import numpy as np
import pandas as pd

col_names = ["y", "desvio_y", "x", "desvio_x"]
amostras = pd.read_csv(
    "experimento_4/dados.dat",
    sep = "\t",
    header = None,
    skiprows = [0],
    names = col_names,
    skipfooter = 3, 
    engine= "python"
)

amostras.desvio_y += 0.001
amostras.y = np.log10(amostras.y)
amostras.desvio_y = np.abs(np.log10(amostras.desvio_y))

definicoes = {
    "a": -0.0240332,
    "b": 1.71573,
    "x_label": "t (s)",
    "y_label": "$log(ddp (V))$",
    "a_legend": "$a = -0,0240 \\pm 0,0004$",
    "b_legend": "$b = 1,716 \\pm 0,004$",
    "text_size" : 6,
    "text_offset_x" : 0,
    "text_offset_y" : 0,
}

# print(amostras)
calcula_grafo.gera_imagem(amostras, "exercicio 4.2", definicoes)

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
