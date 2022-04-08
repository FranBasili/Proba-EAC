import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

file = open("C Resultados.txt","w") # Se guardan los porcentajes de Outliers en un txt
file.write("Porcentajes de Outliers:\n") 
outliersColor = dict(markerfacecolor='b', marker='X')
for aspecto in ['sbp','ldl']:
    q1, q3 = data[aspecto].quantile([0.25, 0.75])
    RI = q3 - q1
    count=0
    for y in range(0, len(data[aspecto])):
        if data[aspecto][y] > q3 + 1.5*RI or data[aspecto][y] < q1 - 1.5*RI:
            count = count + 1
    file.write(aspecto + ": " + str(round(count/len(data[aspecto])*100, 2)) + "%\n") 
    plt.boxplot(data[aspecto], flierprops=outliersColor)
    plt.title(aspecto)
    plt.savefig("C Gráficos\\"+aspecto+".png")
    plt.show()