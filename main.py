import pandas as pd
import os

os.system("pwd")

notas = pd.read_csv('datos/notes.csv', delimiter=";")

print(notas.info)
