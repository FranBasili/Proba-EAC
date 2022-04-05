import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': int, 'chd': bool},
                    skipinitialspace=True)

N = data.shape[0]

bins = {'sbp': 9, 'ldl': 9}

for aspecto in ['sbp','ldl']:

    h, f = np.histogram(data[aspecto], bins=bins[aspecto])

    amp = f[1] - f[0]
    
    h = h / N
    
    f -= amp / 2    # Puntos en el medio
    f = np.append(f, f[-1] + amp)

    h = np.append(h, 0)     # Agregado de 0s en los bordes
    h = np.append([0], h)

    plt.title("Polígono de frecuencias relativas de " + aspecto)
    plt.plot(f, h, 'o-')
    plt.xlabel("Valores de " + aspecto)
    plt.savefig("D Gráficos\\" + aspecto)
    plt.show()