# data_fetcher.py

import pandas as pd
import requests
import config 

"""
Móludo responsavél pela extração e tratamento dos dados obtidos através da API da Alpha Vantage
"""

def obter_dados(symbol):
    """
    Busca dados de preço mensais da ação na Alpha Vantage.
    """
    # ACESSA a chave através do módulo
    if not config.API_KEY_ALPHA:
        print("❌ Erro: API_KEY_ALPHA não está configurada.")
        return None

    print(f"📥 Buscando dados para {symbol}...")
    # ACESSA a chave através do módulo
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={config.API_KEY_ALPHA}"
    
    try:
        response = requests.get(url)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return None

    if "Monthly Time Series" not in data:
        print("❌ Erro: Ação não encontrada ou limite de API Alpha Vantage excedido.")
        return None

    # Transforma o JSON em DataFrame
    df = pd.DataFrame.from_dict(data["Monthly Time Series"], orient='index')
    
    # Limpeza, conversão de tipos e ordenação
    df = df.rename(columns={
        "1. open": "Open", "2. high": "High", "3. low": "Low", 
        "4. close": "Close", "5. volume": "Volume"
    })
    df = df.reset_index().rename(columns={"index": "Data"})
    df['Data'] = pd.to_datetime(df['Data'])
    df = df.sort_values(by='Data')
    
    cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df[cols] = df[cols].apply(pd.to_numeric)
    
    return df