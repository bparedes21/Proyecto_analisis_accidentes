import pandas as pd
def generar_url_descarga_de_achivo(url):

    file_id=url.split('/')[-2]
    dwn_url='https://drive.google.com/uc?id=' + file_id
    return dwn_url

def cortar_columna_fecha(df_,columna):
    df_[columna]=df_[columna].astype('str')
    new2 = df_[columna].str.split(" ", n = 1, expand = True)
    df_[columna]=new2[0]
    return df_  

def nom_empresa(df,empresa):
  
    dfg=pd.DataFrame()
    dfg=df.loc[df['ac_type'].str.contains(empresa)] 

    dfg["empresa"]=empresa
    df.loc[df['ac_type'].str.contains(empresa)] =dfg
    
    return df