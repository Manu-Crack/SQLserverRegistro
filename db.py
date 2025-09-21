import pyodbc

# Cadena de conexión fija para tu caso
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=;"
    "DATABASE=;"
    "UID=;"
    "PWD="
)

def get_connection():
    return pyodbc.connect(conn_str)
 
