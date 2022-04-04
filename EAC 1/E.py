import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

sbp = data['sbp']
ldl = data['ldl']
count = 0
for j in range(0, len(sbp)):
    if (sbp[j] < 130 and ldl[j] < 8):
        count = count + 1
file = open("E Resultados.txt","w") 
file.write("Proporción de muestras:\n")
file.write(str(round(count/len(sbp)*100, 4)) + "%\n")

for i in range(0, len(sbp)):
    plt.plot(ldl[i], sbp[i], 'x',color='blue')
plt.xlabel('LDL')
plt.ylabel('SBP')
plt.title("SBP vs LDL")

plt.axhline(y=130, xmin=0, xmax=0.5, color='r', linestyle='-.', linewidth=2) # Plot a horizontal line using axhline() in pyplot
plt.axvline(x=8, ymin=0, ymax=0.3, color='r', linestyle='-.', linewidth=2)  # Plot a vertical line using axvline() in pyplot
plt.savefig("E Gráficos\\"+"SBPvsLDL"+".png")
plt.show()