import pandas as pd
import Limpieza_y_transformacion_de_datos.funciones_py
import sqlite3


name_db="accidentes_db.db"
conn=sqlite3.connect(name_db)
cursor = conn.cursor()

# Comando SQL para crear una tabla llamada 'Accidentes' 
cursor.execute('''DROP TABLE IF EXISTS Accidentes;''')

create_table_query = '''
CREATE TABLE Accidentes (
    Date TEXT NOT NULL,
    Time INTEGER NOT NULL,
	Ruta INTEGER NOT NULL,
    Operator TEXT,
    Type TEXT,
    all_aboard INTEGER,
    passengers_aboard INTEGER,
    crew_aboard INTEGER,
    all_fatalities	INTEGER,
    passenger_fatalities	INTEGER,
    crew_fatalities INTEGER,
	ground INTEGER,
    summary TEXT,
	año INTEGER,
	empresa TEXT,
	
);
'''

# Comando SQL para crear una tabla llamada 'BoiengHistoricalValue
cursor.execute('''DROP TABLE IF EXISTS BoiengHistoricalValues;''')

create_table_query = '''
CREATE TABLE BoiengHistoricalValues (
    date TEXT,
    open REAL,
	high REAL,
    low REAL,
    close REAL,
    volume REAL,
    año INTEGER
);
'''

conn.commit()

#url_accidentes="https://drive.google.com/file/d/12f2cg41-j0KlOZ5XmYfBbSnnPS-t4WHP/view?usp=sharing"

enlace_descarga_csv_accidentes=Limpieza_y_transformacion_de_datos.funciones_py.generar_url_descarga_de_achivo(url_accidentes)
AccidentesAviones=pd.read_csv(enlace_descarga_csv_accidentes)
AccidentesAviones.to_sql('Accidentes', con=conn, index=False, index_label='Date', if_exists='replace')
conn.commit()
"""
#consulta selecciono todo de la tabla 
query = 'SELECT * FROM Accidentes'
#almaceno en df
df_Accidentes= pd.read_sql(query, conn)
"""
#inserto los datos en la base de datos con SQLite
url_accidentes="https://drive.google.com/file/d/1uNlBJENipat2nGtvC-OFxpmPqSo1B8nZ/view?usp=sharing"
enlace_descarga_csv_acciones=Limpieza_y_transformacion_de_datos.funciones_py.generar_url_descarga_de_achivo(url_accidentes)
Acciones_boing=pd.read_csv(enlace_descarga_csv_acciones)

Acciones_boing.to_sql('BoiengHistoricalValues', con=conn, index=False, index_label='Date', if_exists='replace')
conn.commit()
"""
#consulta selecciono todo de la tabla 
query = 'SELECT * FROM BoiengHistoricalValues'
#almaceno en df
df_BoiengHistoricalValues= pd.read_sql(query, conn)
print(df_BoiengHistoricalValues.head())
"""
conn.close()