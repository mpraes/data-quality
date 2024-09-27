import pandas as pd

def verifica_idades(df):
    df['Verificacao Maior'] = ''
    for i, row in df.iterrows():
        if row['Idade'] < 18:
            df.loc[i, 'Verificacao Maior'] = 'Menor'
        else:
            df.loc[i, 'Verificacao Maior'] = 'Maior'
    return df
        