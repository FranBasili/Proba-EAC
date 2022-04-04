import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

green_diamond = dict(markerfacecolor='b', marker='X')

for aspecto in ['sbp','ldl']:
    plt.boxplot(data[aspecto], flierprops=green_diamond)
    plt.title(aspecto)
    plt.savefig("C Gráficos\ "+aspecto+".png")
    plt.show()