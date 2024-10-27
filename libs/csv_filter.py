import pandas as pd

# Get info from notes.csv, filter it with id_aula, then return the data.
def aula_F(route_to_notes_csv, aula, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["aula_id"] == dv_int(aula)]

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
def dv_int(arr_columns, df):
    for element in arr_columns:
        # Convertir les columnes que necessiten ser numèriques
        df[element] = pd.to_numeric(df[element], errors='coerce')

    return df

# This function returns the average of grades of one student, and also gets the number of evaluations
def dv_avg_ev(id_user):
    activitats = pd.read_csv('../datos/activitats.csv', encoding='latin1')
    trameses = pd.read_csv('../datos/trameses.csv')

    activitats = dv_int(["activitat_id", "aula_id", "startdate", "duedate", "grade"], activitats)
    trameses = dv_int(["id", "activitat_id", "userid", "datesubmitted", "grader", "dategraded", "grade", "nevaluations"], trameses)

    trameses = trameses[trameses["userid"] == id_user]
    # Join trameses with activitats
    trameses_activitats = trameses.merge(activitats, on="activitat_id", how="left")

    trameses_activitats = trameses_activitats.dropna(subset=['grade_x'])

    # Filtrar el intento con la nota más alta para cada actividad y usuario
    highest_grade_attempts = trameses_activitats.loc[
        trameses_activitats.groupby(['userid', 'activitat_id'])['grade_x'].idxmax()
    ]

    # Calculate average and get the ammount of evaluations
    user_activity_summary = highest_grade_attempts.groupby('userid').agg(
        avg_grade_prev=('grade_x', 'mean'),
        num_evaluations=('nevaluations', 'sum')
    ).reset_index()

    return user_activity_summary # Returns [userid,avg_grade_prev,num_evaluations]
