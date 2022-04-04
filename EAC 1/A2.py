import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

sbp = data['sbp']
ldl = data['ldl']
y = 1

for x in range(0, len(sbp)):
    ax = plt.subplot(2,1,1)
    plt.plot(sbp[x], y, 'x',color='blue')
    plt.title("SBP")
    ax.set_xlabel('Presión arterial sistólica')
    ax2 = plt.subplot(2,1,2)
    plt.plot(ldl[x], y,'x', color='blue')	
    ax2.set_xlabel('Colesterol LDL')
    plt.title("LDL")
    plt.tight_layout()

plt.savefig("A Gráficos\\" + "CteVsVM" + ".png")
plt.show()