import pandas as pd
import pandasql as pdsql


def select_first_50(filename):
    aadhaar_data = pd.read_csv(filename)
    aadhaar_data.rename(columns= lambda x: x.replace(' ', '_').lower(), inplace=True)
    q = """
    SELECT registrar, enrolment_agency FROM aadhaar_data LIMIT 50;
    """
    aadhaar_solution = pdsql.sqldf(q.lower(), locals())
    return aadhaar_solution

if __name__ == "__main__":
    print select_first_50('aadhaar_data.csv')
