import pandas as pd
from tabulate import tabulate

file = open("B Resultados.txt","w") 

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

file.write("Resultados:\n")

table = [["Aspecto", "Media", "Mediana", "Desvío Estandar", "Cuartil 1", "Cuartil 3", "Rango Intercuartílico", "Coef. Simetría", "Coef. de Kurtosis"]]

for aspect in ['sbp', 'ldl']:
    m = data[aspect].mean()
    M = data[aspect].median()
    DE = data[aspect].std()
    q1, q3 = data[aspect].quantile([0.25, 0.75])
    RI = q3 - q1
    CS = (q3 - q1)/(q3 + q1)
    K = data[aspect].kurtosis()

    table.append([aspect, round(m, 2), round(M, 2), round(DE, 2), round(q1, 2), round(q3, 2), round(RI, 2), round(CS, 2), round(K, 2)])

file.write(tabulate(table))
file.write("\n\n")
