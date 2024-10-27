import pandas as pd
import regresion_parcial as reg
import csv_filter as csv

iduser = 721

avg_ev = csv.dv_avg_ev(iduser)
notes = pd.read_csv("../datos/notes.csv", delimiter=";")

# Filtrar las notas del usuario
nota = notes[notes["userid"] == iduser]

# Convertir P_Grade a float, reemplazando ',' por '.'
nota['P_Grade'] = nota['P_Grade'].str.replace(',', '.').astype(float)

# Asegúrate de que hay al menos un valor de P_Grade
if not nota.empty and nota["P_Grade"].notna().any():
    p_grade_value = nota["P_Grade"].iloc[0]  # Obtener el primer valor de P_Grade

    # Obtener los valores escalares para avg_grade_prev y num_evaluations
    avg_grade_prev = avg_ev["avg_grade_prev"].iloc[0]  # Asegúrate de que esto sea un solo valor
    num_evaluations = avg_ev["num_evaluations"].iloc[0]  # Asegúrate de que esto sea un solo valor

    # Imprimir valores para depuración
    print("P_Grade:", p_grade_value)
    print("avg_grade_prev:", avg_grade_prev)
    print("num_evaluations:", num_evaluations)

    # Llamar a la función con valores individuales
    result = reg.get_final(avg_grade_prev, num_evaluations, p_grade_value)

    print("Resultado:", result)
else:
    print("No hay notas disponibles para el usuario o P_Grade es nulo.")
