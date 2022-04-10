import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

GrupoA=data[(data['chd'] == False) & (data['famhist'] == True)]     # No tiene enfermedad ni antecedentes 
GrupoB=data[((data['chd'] == True) & (data['famhist'] == True)) | # No tiene enfermedad pero sí antecedentes
            ((data['chd'] == False) & (data['famhist'] == False))]    # Tiene enfermedad pero no antecedentes
GrupoC=data[(data['chd'] == True) & (data['famhist'] == False)]     # Tiene antecedentes y la enfermedad

for aspecto in ["sbp","ldl",'tipo A']:
    data = pd.concat([GrupoA[aspecto].rename("Grupo A"), GrupoB[aspecto].rename("Grupo B"), GrupoC[aspecto].rename("Grupo C")], 
                    ignore_index=False, axis=1)
    shape = data.shape              
    hist=data.plot.hist(bins=math.ceil(math.log(shape[0])), alpha=0.3)
    hist.set_ylabel("Frecuencia")
    hist.set_xlabel(aspecto)
    hist.plot()
    plt.title(aspecto)
    plt.savefig("I Gráficos\\" + aspecto + ".png")
    plt.show()