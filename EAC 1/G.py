import pandas as pd
from tabulate import tabulate

file = open("G Resultados.txt","w") 

data = pd.read_table("heart2022.txt", sep=' ', names=['sbp', 'ldl', 'famhist', 'tipo A', 'chd'],
                    dtype={'sbp': int, 'ldl': float, 'famhist': bool, 'tipo A': float, 'chd': bool})

GrupoA=data[(data['chd'] == False) & (data['famhist'] == True)]     # No tiene enfermedad ni antecedentes 
GrupoB=data[((data['chd'] == False) & (data['famhist'] == False)) | # No tiene enfermedad pero sí antecedentes
            ((data['chd'] == True) & (data['famhist'] == True))]    # Tiene enfermedad pero no antecedentes
GrupoC=data[(data['chd'] == True) & (data['famhist'] == False)]     # Tiene antecedentes y la enfermedad

for Group in [GrupoA, GrupoB, GrupoC]:
    
    if Group.equals(GrupoA):
        file.write("Grupo A:\n")
    elif Group.equals(GrupoB):
        file.write("Grupo B:\n")
    else:
        file.write("Grupo C:\n")
    
    table = [["Aspecto", "Cuartil 1", "Cuartil 3"]]

    for aspect in ['sbp', 'ldl', 'tipo A']:
        q1, q3 = Group[aspect].quantile([0.25, 0.75])
        table.append([aspect, round(q1), round(q3)])

    file.write(tabulate(table))
    file.write("\n\n")


