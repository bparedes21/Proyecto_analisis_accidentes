import pandas as pd
import numpy as np
from datetime import datetime
import funciones_py

def transformar_df_aviones(df_accidentes):
    #creo una nueva columna para agrupar las empresas con mas accidentes y las que tienen menos accidentes
    #quedan en la categoria otra empresa
    df_accidentes["empresa"]="Otra empresa"
    list_empresa=[]
    list_empresa=["Douglas", "Boeing","Lockheed","Yakovlev","Antonov","de Havilland Canada","Breguet","Junkers","De Havilland"]

    for empresa in list_empresa:
        df_new=funciones_py.nom_empresa(df_accidentes,empresa)
        df_accidentes=pd.DataFrame()
        df_accidentes=df_new
    #normalizo el nombre de las empresas que son iguales pero se llaman distinto
    df_accidentes["empresa"] =df_accidentes["empresa"].replace("de Havilland Canada","De Havilland")

    #renombro las columnas para darle mas congruencia con los datos que contienen
    df_accidentes.rename(columns={'fecha':'Date','HORA declarada':'Time',"Location":"Ruta","OperadOR":"Operator","route":"Route","ac_type":"Type","Aboard":"all_aboard","PASAJEROS A BORDO":"passengers_aboard","cantidad de fallecidos":"all_fatalities"},
               inplace=True)
    #reemplazo ? por nan, veo cuantos registos hay sin valor
    #rep = {}
    new_df =df_accidentes.replace("?",np.nan)
    df_accidentes=pd.DataFrame()
    df_accidentes=new_df.copy()

    
    #borro las columnas que no voy a utilizar
    new_df1=df_accidentes.drop(columns=["Unnamed: 0","flight_no","registration", "cn_ln","Route"])
    df_accidentes=pd.DataFrame()
    df_accidentes=new_df1.copy()
    #Cambio el tipo de dato de la columna date
    df_accidentes["Date"]=pd.to_datetime(df_accidentes["Date"])
    
    #agrego la columna "año" (year)
    df_accidentes["año"]=df_accidentes.Date.dt.year
    
    """ 
    list_hora=[]
 
    #pongo ":" a hora y reemplazo nan por 00:00 en la columna Time
    df_accidentes["Time"]=df_accidentes["Time"].astype('str')
    #
    list_hora=df_accidentes["Time"]

    for i,hora in enumerate(list_hora):
    
        if (hora[2]==":" or hora=="nan"):
            continue
        else:
            
            hora = hora[:2] + ':' + hora[2:]
            list_hora[i]=hora
    """     
    
    #df_accidentes.loc[df_accidentes['Type'].str.contains('Douglas')]
    #avion de boing con mas accidentes Boeing 40
    #dfg=df_accidentes.loc[~df_accidentes['Type'].str.contains('Boeing') ]
    #df_Boeing.Type.value_counts()

    #borro los faltantes
    df_1=df_accidentes.dropna()
    df_accidentes=pd.DataFrame()
    df_accidentes=df_1
    return df_accidentes

    
        