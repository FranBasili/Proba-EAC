import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

GrupoA=data[(data['chd'] == False) & (data['famhist'] == True)]     # No tiene enfermedad ni antecedentes 
GrupoB=data[((data['chd'] == False) & (data['famhist'] == False)) | # No tiene enfermedad pero sí antecedentes
            ((data['chd'] == True) & (data['famhist'] == True))]    # Tiene enfermedad pero no antecedentes
GrupoC=data[(data['chd'] == True) & (data['famhist'] == False)]     # Tiene antecedentes y la enfermedad

for aspecto in ["sbp","ldl",'tipo A']:
    data = pd.concat([GrupoA[aspecto].rename("Grupo A"), GrupoB[aspecto].rename("Grupo B"), GrupoC[aspecto].rename("Grupo C")], 
                    ignore_index=False, axis=1) 
    boxplot=data.boxplot()
    boxplot.plot()
    plt.title(aspecto)
    plt.savefig("H Gráficos\\"+aspecto+".png")
    plt.show()