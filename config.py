# config.py

"""
Módulo de Configuração Centralizado, onde as chavem das APIs são carregadas e os clientes são inicializados.
"""

import os
# Garante que o .env seja carregado assim que o módulo for importado
from dotenv import load_dotenv
from google import genai

# Obtém o caminho base do diretório atual do config.py
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# 1. Carrega  Variáveis de Ambiente
# A linha load_dotenv é movida para cá para garantir que seja executada 
# no momento da importação do módulo config.
load_dotenv(os.path.join(BASEDIR, '.env'))


# 2. Obter Chaves de API (Variáveis Globais)
# Obtém as chaves que foram carregadas do .env.
API_KEY_ALPHA = os.getenv("API_KEY_ALPHA")
API_KEY_GEMINI = os.getenv("API_KEY_GEMINI")


# 3. Inicializar Clientes de API
# O cliente é inicializado APENAS AQUI.
client = None
if API_KEY_GEMINI:
    try:
        client = genai.Client(api_key=API_KEY_GEMINI)
        # Se a chave for inválida ou o cliente não puder ser criado, client permanece None.
    except Exception as e:
        # Nota: Idealmente, essa mensagem de erro seria mostrada se a API_KEY não funcionar
        # Mas o erro mais comum aqui é se a API_KEY for fornecida, mas estiver errada.
        print(f"❌ Erro ao inicializar o cliente Gemini. Verifique a chave em .env: {e}")