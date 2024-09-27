import pandas as pd

def verifica_idades(df):
    for i in df['Idade']:
        df['Msg'] = 'NaN'
        if i < 18:
            return df["Msg"] == 'Menor de idade'
        else:
            return df["Msg"] == 'Maior de idade'