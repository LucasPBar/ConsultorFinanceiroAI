# visualizer.py

"""
Módulo responsável pela visualização dos dados financeiros e indicadores técnicos.
"""

import pandas as pd
import matplotlib.pyplot as plt

def exibir_tabela_resumo(df):
    """
    Exibe uma tabela simples com indicadores chave no console.
    """
    if df is None or len(df) < 24: # Mínimo 2 anos de dados para análise
        print("\n⚠️ Dados insuficientes para análise de longo prazo (mínimo 2 anos).")
        return

    # Pega o último e o valor de 1 ano atrás
    ultimo = df.iloc[-1]
    anterior_12m = df.iloc[-13] if len(df) >= 13 else df.iloc[0]

    # Cria o DataFrame para a tabela
    resumo = pd.DataFrame({
        'Indicador': ['Preço Atual', 'Preço há 1 Ano', 'Média Móvel (12m)', 'Média Móvel (24m)', 'RSI Atual', 'Volume Atual'],
        'Valor': [
            f"${ultimo['Close']:.2f}",
            f"${anterior_12m['Close']:.2f}",
            f"${ultimo['SMA_12']:.2f}",
            f"${ultimo['SMA_24']:.2f}",
            f"{ultimo['RSI']:.2f} pontos",
            f"{int(ultimo['Volume']):,}".replace(",", ".") # Formata volume
        ]
    })
    
    print("\n📊 TABELA DE DADOS FUNDAMENTAIS")
    print("="*40)
    print(resumo.to_string(index=False, justify='left')) 
    print("="*40)


def gerar_dashboard(df, symbol):
    """
    Gera o dashboard visual (Preço, Volume e RSI) com matplotlib.
    """
    if df is None or df.empty:
        print("Não foi possível gerar o dashboard devido à falta de dados.")
        return
        
    # Filtra os últimos 4 anos para não poluir o gráfico
    df_chart = df.tail(48).copy() 
    
    # Cria uma figura com 3 gráficos empilhados
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 1, height_ratios=[3, 1, 1])

    # GRÁFICO 1: Preço e Médias
    ax1 = fig.add_subplot(gs[0])
    ax1.plot(df_chart['Data'], df_chart['Close'], label='Preço Atual', color='black', linewidth=2)
    ax1.plot(df_chart['Data'], df_chart['SMA_12'], label='Média 1 ano (Curto Prazo)', color='green', linestyle='--')
    ax1.plot(df_chart['Data'], df_chart['SMA_24'], label='Média 2 anos (Longo Prazo)', color='red', linestyle='--')
    ax1.set_title(f'Análise de Tendência: {symbol}', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Preço ($)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # GRÁFICO 2: Volume
    ax2 = fig.add_subplot(gs[1], sharex=ax1)
    colors = ['green' if x >= 0 else 'red' for x in df_chart['Close'].diff()]
    ax2.bar(df_chart['Data'], df_chart['Volume'], color=colors, alpha=0.6)
    ax2.set_ylabel('Volume')
    ax2.grid(True, alpha=0.3)
    ax2.legend(['Volume de Negociação'], loc='upper left')

    # GRÁFICO 3: RSI 
    ax3 = fig.add_subplot(gs[2], sharex=ax1)
    ax3.plot(df_chart['Data'], df_chart['RSI'], color='purple', label='RSI')
    ax3.axhline(70, color='red', linestyle=':', linewidth=1) 
    ax3.axhline(30, color='green', linestyle=':', linewidth=1) 
    ax3.fill_between(df_chart['Data'], 70, 30, color='gray', alpha=0.1)
    ax3.set_ylabel('RSI (0-100)')
    ax3.set_xlabel('Data')
    ax3.legend(loc='upper left')
    
    plt.tight_layout()
    plt.show() # Exibe a janela de gráficos