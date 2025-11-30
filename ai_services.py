# ai_services.py

"""
Módulo responsável pelos serviços de IA utilizando a API Gemini.
"""

import config # Importa o módulo de configuração
import pandas as pd 

# Função de análise de ação utilizando IA
def analise_ia(df, symbol):
    """
    Gera uma análise técnica e fundamentalista simplificada com Gemini.
    """
    # Acessa o cliente através do módulo client oriundo da config
    if config.client is None:
        print("❌ Erro: Cliente Gemini não inicializado. Verifique a API_KEY.")
        return
        
    last = df.iloc[-1] 
    
    # Preparação dos dados 
    tendencia = "ALTA" if last['Close'] > last['SMA_12'] else "BAIXA"
    momentum = "NEUTRO"
    if last['RSI'] > 70: momentum = "ESTICADO (Pode cair)"
    elif last['RSI'] < 30: momentum = "BARATO (Pode subir)"

    prompt = f"""
    Você é um analista financeiro educador. Faça um RESUMO de longo prazo sobre a ação {symbol}, com linguagem simples e clara para iniciantes.

    Comece explicando brevemente:
    “O que é essa empresa e qual seu papel no mercado?”

    Use SOMENTE os dados abaixo (retirados dos gráficos e da tabela):

    DADOS DO ATIVO:
    - Preço Atual: ${last['Close']:.2f}
    - Tendência com base nas Médias: {tendencia}
    - Média Móvel 12 meses: {last['SMA_12']:.2f}
    - Média Móvel 24 meses: {last['SMA_24']:.2f}
    - RSI Atual: {last['RSI']:.2f} → {momentum}
    - Volume Atual: {last['Volume']}

    Diretrizes obrigatórias:
    - A análise deve ser de LONGO PRAZO.
    - Escreva em formato de RESUMO.
    - NÃO faça análise de curto prazo.
    - NÃO gere recomendação de compra ou venda.
    - NÃO use termos como “compre”, “venda” ou “invista”.
    - Caso algum dado de fundamentos não esteja disponível, apenas faça uma leitura técnica baseada no preço, médias e RSI.
    - A classificação final deve ser apenas uma destas: Fraco, Regular, Bom ou Excelente.

    A estrutura da resposta deve ser:

    1. O que é a empresa (bem curto)
    2. Leitura técnica de longo prazo (preço, médias e RSI)
    3. Pontos fortes e riscos
    4. Classificação final para o longo prazo

    Finalize obrigatoriamente com este aviso:

    “Esta análise possui exclusivamente finalidade educacional e não representa qualquer recomendação de compra ou venda de ativos financeiros.”
    """


    print("\n🤖 ANALISANDO OS DADOS...")
    try:
        # Usa config.client
        response = config.client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        print("-" * 60)
        print(response.text)
        print("-" * 60)
    except Exception as e:
        print(f"Erro na API do Gemini: {e}")

# Função de assistente financeiro para responder perguntas sobre finanças/investimentos
def conversar_com_ia_financeira():
    """
    Permite ao usuário fazer perguntas gerais, validando se são sobre finanças/investimentos.
    """
    # Acessa o cliente através do módulo client oriundo da config
    if config.client is None:
        print("❌ Erro: Cliente Gemini não inicializado. Verifique a API_KEY.")
        return

    pergunta = input("\n❔ Digite sua dúvida sobre investimentos/finanças: ")
    
    # Prompt utilizado para validar o tópico da pergunta solicitado pelo usuário
    prompt_qa = f"""
    Você é um assistente financeiro. Responda apenas a perguntas relacionadas a finanças, 
    economia, investimentos, mercado de ações e educação financeira.
    
    Se a pergunta do usuário **NÃO** for sobre finanças/investimentos/economia, 
    responda **EXATAMENTE** com a frase: 'TÓPICO INVÁLIDO'
    
    Pergunta do Usuário: {pergunta}
    """
    
    print("\n🤖 Pensando...")
    try:
        # Usa config.client
        response = config.client.models.generate_content(model='gemini-2.5-flash', contents=prompt_qa)
        resposta_ia = response.text.strip()
        
        if resposta_ia == 'TÓPICO INVÁLIDO':
            print("\n❌ ERRO: Sua pergunta não está relacionada a investimentos ou finanças. Tente novamente.")
        else:
            print("\n" + "="*60)
            print("Resposta do Consultor Financeiro:")
            print(resposta_ia)
            print("="*60)
            
    except Exception as e:
        print(f"Erro na API do Gemini: {e}")