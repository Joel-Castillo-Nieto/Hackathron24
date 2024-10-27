import pandas as pd

def full_csv(route_to_notes_csv, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)
    return csv_data

def csv_aula_F(route_to_notes_csv, aula, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["aula_id"] == int(aula)]

    return csv_clean

def csv_partial_F(route_to_notes_csv, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["P_Grade"].notna()]

    return csv_clean

def csv_no_partial_F(route_to_notes_csv, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_clean = csv_data[csv_data["P_Grade"].notna() == False]

    return csv_clean

def csv_partial_R(route_to_notes_csv, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].notna()]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean

def csv_no_partial_R(route_to_notes_csv, delim=","):
    csv_data = pd.read_csv(route_to_notes_csv, delimiter=delim)

    csv_data = csv_data[csv_data["F_Grade"].notna()]
    csv_data = csv_data[csv_data["P_Grade"].notna() == False]
    csv_clean = csv_data[csv_data["R_Grade"].notna()]

    return csv_clean







csv_no_partial_R("../datos/notes.csv",";")