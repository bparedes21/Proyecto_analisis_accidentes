import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlite3

def get_database_connection():
    
    mi_conexion=sqlite3.connect("miprimera.bd")
    return mi_conexion
#creo la tabla AccidentesAviones e inserto los datos en la base de datos con SQLite
mi_conexion=get_database_connection()
AccidentesAviones=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\pi03\PI03-Analytics\AccidentesAviones_csv.csv')
AccidentesAviones.to_sql('AccidentesAviones', con=mi_conexion, index=False, index_label='id', if_exists='replace')
mi_conexion.commit()
mi_conexion.close()
#creo la tabla e inserto los datos en la base de datos con SQLite
mi_conexion=get_database_connection()
AccidentesAviones=pd.read_csv(r'C:\Users\ROXI\OneDrive\Escritorio\pi03\PI03-Analytics\MacroTrends.csv')
AccidentesAviones.to_sql('BoiengHistoricalValues', con=mi_conexion, index=False, index_label='id', if_exists='replace')
mi_conexion.commit()
mi_conexion.close()