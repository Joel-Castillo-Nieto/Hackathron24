import pandas as pd
from libs import info, regresion_parcial as reg, csv_filter as csv

coeficients = reg.get_reg()

trameses = pd.read_csv("./datos/trameses.csv")

trameses = csv.int(["id","activitat_id","userid","datesubmitted","grader","dategraded","grade","nevaluations"],trameses)


