from app.main import verifica_idades
import pandas as pd
from pandas.testing import assert_frame_equal

def test_verifica_idades():
    # DataFrame de exemplo
    data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
            'Idade': [15, 22, 17, 30]}
    df = pd.DataFrame(data)
    
    # DataFrame esperado após a verificação de idades
    expected_data = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
                     'Idade': [15, 22, 17, 30],
                     'Verificacao Maior': ['Menor', 'Maior', 'Menor', 'Maior']}
    expected_df = pd.DataFrame(expected_data)

    # Executa a função que será testada
    result_df = verifica_idades(df)

    # Verifica se o resultado é igual ao DataFrame esperado
    assert_frame_equal(result_df, expected_df)