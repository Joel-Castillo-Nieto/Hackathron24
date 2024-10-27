import pandas as pd

# Get info from notes.csv, filter it with id_aula, then return the data.
def aula_F(route_to_notes_csv, aula, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["aula_id"] == int(aula)]

    return csv_clean

# Pass the data filtered (for example with aula_F()) then returns it with the
# students that did the Partial Exam and Final Exam.
def partial_F(pd_data):
    csv_clean = pd_data[pd_data["F_Grade"].notna()]
    csv_clean = csv_clean[csv_clean["P_Grade"].notna()]

    return csv_clean

# The same as partial_F but with students that didn't do the partial.
def no_partial_F(pd_data):
    csv_data = pd_data[pd_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["P_Grade"].isna()]

    return csv_clean

# Pass the data filtered (for example with aula_F()) then filter
# all null in grades.
def partial_R(pd_data):
    csv_data = pd_data[pd_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].notna()]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean


# The same as partial_R but with partial being null and other grades
# filtering the NULL
def no_partial_R(pd_data):
    csv_data = pd_data[pd_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].isna()]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean

# This function, gets the values and removes the "" to turn them into numbers.
def int(arr_columns,df):
    for element in arr_columns:
        # Convertir les columnes que necessiten ser numèriques
        df[element] = pd.to_numeric(df[element], errors='coerce')

    return df


def avg_grade(id_user, ruta_csv='../datos/trameses.csv', delim=","):
    trameses = pd.read_csv(ruta_csv, sep=delim)

    # Filter rows for student
    trameses_usuario = trameses[trameses["userid"] == id_user]

    # Transform values into integer
    trameses_usuario = int(["userid","grade","nevaluations"],trameses_usuario)

    # Get the average grade, ignoring null values
    trameses_usuario = trameses_usuario[trameses_usuario['grade'].notna()]
    nota_media = trameses_usuario['grade'].mean()

    return nota_media

print(avg_grade(128))