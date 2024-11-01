# Importamos las bibliotecas necesarias
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def get_reg():
    # Cargar los datos
    notes = pd.read_csv('../datos/notes.csv', sep=';')
    activitats = pd.read_csv('../datos/activitats.csv', sep=',', encoding='latin1')
    trameses = pd.read_csv('../datos/trameses.csv', sep=',')

    # Unir trameses con activitats
    trameses_activitats = trameses.merge(activitats, on="activitat_id", how="left")

    trameses_activitats = trameses_activitats.dropna(subset=['grade_x'])

    # Filtrar el intento con la nota más alta para cada actividad y usuario
    highest_grade_attempts = trameses_activitats.loc[
        trameses_activitats.groupby(['userid', 'activitat_id'])['grade_x'].idxmax()
    ]

    # Calcular el promedio de las calificaciones de las actividades y el total de intentos por usuario
    user_activity_summary = highest_grade_attempts.groupby('userid').agg(
        avg_grade_prev=('grade_x', 'mean'),
        num_evaluations=('nevaluations', 'sum')
    ).reset_index()

    # Unir el resultado con notes, de modo que cada usuario tenga una sola fila
    data = notes.merge(user_activity_summary, on="userid", how="left")

    # Eliminar filas donde P_Grade sea nulo
    data = data.dropna(subset=['P_Grade'])

    # Reemplazar comas por puntos y convertir a float
    data['P_Grade'] = data['P_Grade'].str.replace(',', '.').astype(float)
    data['F_Grade'] = data['F_Grade'].str.replace(',', '.').astype(float)

    # Seleccionar solo las columnas necesarias para el modelo
    df = data[['userid', 'F_Grade', 'avg_grade_prev', 'num_evaluations', 'P_Grade']].dropna()

    # Dividir los datos en características (X) y variable objetivo (Y)
    X = df[['avg_grade_prev', 'num_evaluations', 'P_Grade']]
    Y = df['F_Grade']

    # Dividir en conjunto de entrenamiento y prueba
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Crear y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Obtener los coeficientes (w1, w2, w3) y el intercepto (b)
    coefficients = model.coef_  # Coeficientes (w1, w2, w3)
    intercept = model.intercept_  # Intercepto (b)

    # print("Coeficientes:", coefficients)
    # print("Intercepto:", intercept)

    return [coefficients[0],coefficients[1],coefficients[2],intercept]

def get_final(arg_grade,num_eva,p_grade):
    coeficients = get_reg()
    result = (float(arg_grade)*coeficients[0])+(num_eva*coeficients[1])+(p_grade*coeficients[2])+(coeficients[3])
    return result

# print(get_final(99.999,150,7))