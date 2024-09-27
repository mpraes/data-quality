from app.main import verifica_idades
import pandas as pd

df = pd.DataFrame({'Id': [1, 2], 'Nome': ['Renan', 'Maria'], 'Idade': [37, 6]})

df = verifica_idades(df)