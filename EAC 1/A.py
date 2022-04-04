import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

sbp = data['sbp']
ldl = data['ldl']

ax = plt.subplot(2,1,1)
plt.plot(sbp, '.')
plt.title("SBP")
ax.set_ylabel('Presión arterial sistólica')
ax2 = plt.subplot(2,1,2)
plt.plot(ldl, '.')
ax2.set_xlabel('Número de muestras')
ax2.set_ylabel('Colesterol LDL')
plt.title("LDL")
plt.tight_layout()
plt.savefig("A Gráficos\ "+"SdTiempo"+".png")
plt.show()