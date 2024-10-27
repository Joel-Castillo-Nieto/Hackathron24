import pandas as pd
import csv_filter as csv, regresion_parcial as reg

def recomana_activitats():
    trameses = pd.read_csv("../datos/trameses.csv")
    activitats = pd.read_csv("../datos/activitats.csv")

    trameses = csv.int(["id","activitat_id","userid","datesubmitted","grader","dategraded","grade","nevaluations"],trameses)
    activitats = csv.int(["activitat_id", "aula_id", "startdate", "duedate", "grade"], activitats)

    trameses_activitats = trameses.merge(activitats, on="activitat_id", how="left")