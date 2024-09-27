from app.main import verifica_idades
import pandas as pd

def test_verifica_idades():
    df = pd.DataFrame()
    df['Idade'] = [18, 22]
    df['Verificacao Maior'] = ['Maior', 'Maior']
    assert verifica_idades(df)
    