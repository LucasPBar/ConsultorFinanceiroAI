# processing.py

"""
Módulo de processamento dos dados financeiros para o cálculo de indicadores técnicos.
"""

import pandas as pd

def calcular_indicadores(df):
    """
    Calcula as Médias Móveis (SMA) de 12 e 24 meses e o RSI de 14 períodos.
    """
    if df is None or df.empty:
        return df
        
    # Médias Móveis (Tendência)
    df['SMA_12'] = df['Close'].rolling(window=12).mean() # Média móvel de 1 ano
    df['SMA_24'] = df['Close'].rolling(window=24).mean() # Média móvel de 2 anos
    
    # RSI (Momentum - Força do movimento)
    delta = df['Close'].diff() 
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df