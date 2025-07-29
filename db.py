import pyodbc

# Cadena de conexión fija para tu caso
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-7S23QS1\\SQLEXPRESS2017;"
    "DATABASE=flaskContacto;"
    "UID=sa;"
    "PWD=Ratas1234"
)

def get_connection():
    return pyodbc.connect(conn_str)
 