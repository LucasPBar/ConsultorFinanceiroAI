# main.py

"""
Ponto de entrada principal do sistema de Consultor Financeiro AI.
Gerencia o fluxo de interação com o usuário e orquestra os módulos de aquisição, processamento
e visualização de dados, além dos serviços de IA.
"""

# Importa as funções dos módulos de serviço
from data_fetcher import obter_dados
from processing import calcular_indicadores
from visualizer import exibir_tabela_resumo, gerar_dashboard
from ai_services import analise_ia, conversar_com_ia_financeira

# Estrutura de interação com o usuário
def main_menu():
    """
    Estrutura de loop principal para interação com o usuário (Permite múltiplas ações).
    """
    while True:
        print("\n" + "—"*60)
        print("MENU PRINCIPAL - CONSULTOR FINANCEIRO AI")
        print("—"*60)
        print("1. 📈 Analisar Ação (Gráficos, Indicadores e Parecer IA)")
        print("2. ❓ Perguntar sobre Finanças/Investimentos (Dúvidas gerais)")
        print("3. 🚪 Sair do Sistema")
        print("—"*60)
        
        escolha = input("Selecione uma opção (1, 2 ou 3): ")

        # Função de análise de ação utilizando IA
        if escolha == '1':
            symbol = input("\nDigite o símbolo da ação (ex: IBM, AAPL): ").upper() # Garante maiúsculas
            
            # 1. Aquisição
            df = obter_dados(symbol)
            
            if df is not None:
                # 2. Processamento
                df = calcular_indicadores(df)
                
                # 3. Visualização
                exibir_tabela_resumo(df)
                gerar_dashboard(df, symbol)
                
                # 4. Análise de IA
                analise_ia(df, symbol)
        
        # Função de assistente financeiro para responder perguntas sobre finanças/investimentos   
        elif escolha == '2':
            conversar_com_ia_financeira()
        
        # Encerramento do programa
        elif escolha == '3':
            print("\n👋 Obrigado por usar o Consultor Financeiro AI. Até logo!")
            break
            
        else:
            # Opção Inválida
            print("\n⚠️ Opção inválida. Por favor, digite 1, 2 ou 3.")

# Início do programa
if __name__ == "__main__":
    main_menu()