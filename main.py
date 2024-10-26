import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Paso 1: Cargar los archivos CSV
activitats_df = pd.read_csv('./datos/activitats.csv', delimiter=',', encoding='ISO-8859-1')
trameses_df = pd.read_csv('./datos/trameses.csv', delimiter=',', encoding='ISO-8859-1')
notes_df = pd.read_csv('./datos/notes.csv', delimiter=';', encoding='ISO-8859-1')

# Paso 2: Procesar y agregar datos relevantes
# Calcular el promedio de notas en actividades y el número total de intentos para cada usuario

# Cambiar el nombre de grader a userid
trameses_df.rename(columns={'grader': 'userid'}, inplace=True)

activitats_agg = trameses_df.groupby('userid').agg({
    'grade': 'mean',           # Promedio de notas en actividades
    'nevaluations': 'sum',     # Total de intentos
    'activitat_id': 'nunique'  # Número de actividades completadas
}).rename(columns={
    'grade': 'avg_activity_score',
    'nevaluations': 'total_attempts',
    'activitat_id': 'total_activities'
})

# Paso 3: Unir esta información con las notas de los exámenes en notes_df
# Filtrar para solo obtener la nota final o parcial deseada (suponiendo que queremos predecir `F_Grade`)
data = pd.merge(notes_df, activitats_agg, on='userid', how='inner')

# Filtrar solo las columnas necesarias para el modelo
data = data[['userid', 'avg_activity_score', 'total_attempts', 'total_activities', 'F_Grade']]

# Eliminar filas con valores nulos en la columna de la nota final
data = data.dropna(subset=['F_Grade'])

# Paso 4: Preparar datos para el modelo
X = data[['avg_activity_score', 'total_attempts', 'total_activities']]
y = data['F_Grade']

# División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 5: Entrenar el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo con el conjunto de prueba
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio (MSE): {mse:.2f}')

# Paso 6: Función para predecir la nota de un nuevo estudiante usando un archivo CSV de entrada
def predict_grade_for_new_student(csv_path):
    new_data = pd.read_csv(csv_path)

    # Procesar los datos del nuevo archivo de la misma forma
    new_activitats_agg = new_data.groupby('userid').agg({
        'grade': 'mean',
        'nevaluations': 'sum',
        'activitat_id': 'nunique'
    }).rename(columns={
        'grade': 'avg_activity_score',
        'nevaluations': 'total_attempts',
        'activitat_id': 'total_activities'
    })

    # Usar solo las columnas relevantes para hacer la predicción
    X_new = new_activitats_agg[['avg_activity_score', 'total_attempts', 'total_activities']]

    # Predecir la nota para el examen final
    predicted_grades = model.predict(X_new)
    return predicted_grades

# Ejemplo de uso con un archivo CSV de un alumno
predicted_grade = predict_grade_for_new_student('./datos/test.csv')
print(f'Nota estimada para el próximo examen: {predicted_grade[0]:.2f}')
