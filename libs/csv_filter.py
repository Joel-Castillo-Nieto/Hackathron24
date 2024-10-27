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
    csv_clean = csv_data[csv_data["P_Grade"].notna() == False]

    return csv_clean

# Pass the data filtered (for example with aula_F()) then r
def partial_R(pd_data):
    csv_data = pd_data[pd_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].notna()]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean

def no_partial_R(pd_data):
    csv_data = pd_data[pd_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].notna() == False]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean