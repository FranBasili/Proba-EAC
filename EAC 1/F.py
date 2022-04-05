import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': int, 'chd': bool},
                    skipinitialspace=True)

N = data.shape[0]

i = 1

for aspecto in ['sbp', 'ldl', 'tipo A']:
    for cond in [False, True]:

        x = data[data.chd == cond][aspecto].values

        x.sort()    # Ordenar los datos
        y = np.array(range(1, len(x)+1)) / len(x)   # y = i/n

        plt.subplot(2, 3, i)
        plt.title("Distribución empírica de " + aspecto + (" con" if cond else " sin") + " chd")
        plt.xlabel(aspecto)
        plt.plot(x, y, 'o-', label=("con" if cond else " sin") + " chd")
        # plt.savefig("F Gráficos\\" + aspecto + '_' + str(cond))
        # plt.show()
        i += 3
    # plt.legend()
    # plt.savefig("F Gráficos\\" + aspecto)
    # plt.show()
    i -= 5
        
# plt.get_current_fig_manager().full_screen_toggle()
plt.get_current_fig_manager().window.showMaximized()
plt.tight_layout()
# plt.savefig("F Gráficos\\Total")
plt.show()