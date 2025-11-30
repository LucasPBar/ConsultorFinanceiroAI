 <div align="center">
  <h1>Projeto ETL Financeiro com Análise de Ações via IA</h1>
  <p><strong>Desafio DIO + Santander 2025 • Ciência de Dados com Python</strong></p>
</div>
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/ETL-Process-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/IA-Gemini-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/API-Alpha%20Vantage-green?style=for-the-badge">
  <br><br>
</div>

![Image](https://github.com/user-attachments/assets/589836a8-6eaa-4119-a4bf-8338cfbdc1cd)


---

## 📌 Contexto do Projeto

<div style="background-color:#f6f8fa; padding:15px; border-radius:10px;">
Este projeto foi desenvolvido como parte do desafio proposto no bootcamp <strong>"Santander 2025 - Ciência de Dados com Python"</strong>, promovido pela <strong>DIO (Digital Innovation One)</strong> em parceria com o <strong>Santander</strong>.
</div>

Este projeto envolve a construção de um pipeline de ETL para o **mercado financeiro**, aplicando os conceitos de ETL sobre **dados reais de ações americanas**, integrando também uma camada de **Inteligência Artificial para geração de análises estratégicas**.

## 🧱 Arquitetura do Sistema

<div style="background-color:#f6f8fa; padding:15px; border-radius:10px;">
O sistema foi estruturado em camadas, simulando um fluxo real de dados em produção:
</div>

1️⃣ Entrada do usuário (Ticker ou pergunta)  
2️⃣ Camada de extração via API Alpha Vantage  
3️⃣ Camada de transformação e tratamento dos dados  
4️⃣ Camada de integração com IA (Gemini)  
5️⃣ Camada de resposta ao usuário  

Esse modelo garante **escalabilidade, organização e separação de responsabilidades** dentro do projeto.

---

## 🎯 1. Sobre o Projeto

### 1.1 O que consiste o projeto?

O projeto consiste em um sistema que:

- Extrai dados financeiros de ações da bolsa americana via API da Alpha Vantage  
- Realiza o tratamento e padronização desses dados  
- Envia as informações tratadas para uma IA  
- Retorna ao usuário uma **análise automatizada e personalizada de longo prazo**
- Disponibiliza também um **assistente de investimentos interativo**

---

### 1.2 Qual é o objetivo do projeto?

O objetivo central é **demonstrar, na prática, todas as etapas de um processo de ETL (Extract, Transform, Load)**, aplicadas em um cenário real de mercado financeiro, integrando:

- Coleta de dados reais  
- Tratamento de dados  
- Aplicação de Inteligência Artificial  
- Entrega de valor direto ao usuário final  

---

### 1.3 Quais ferramentas foram utilizadas?

<div style="display:flex; gap:12px; flex-wrap:wrap; align-items:center;">
  <!-- Card Python -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:220px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#3776AB" d="M12 2L2 7l10 5 10-5-10-5z"></path></svg>
      <div>
        <strong>Python</strong><br><small>Ambiente e scripts</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">Versão alvo: <strong>3.10+</strong></p>
  </div>

  <!-- Card Pandas -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:220px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#150458" d="M12 2l10 6-10 6-10-6z"></path></svg>
      <div>
        <strong>Pandas</strong><br><small>Manipulação de dados</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">DataFrames para limpeza e transformação</p>
  </div>

  <!-- Card Requests -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:220px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#6c757d" d="M12 2l9 7-9 7-9-7z"></path></svg>
      <div>
        <strong>Requests</strong><br><small>Chamadas HTTP</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">Comunicação com Alpha Vantage</p>
  </div>

  <!-- Card Jupyter -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:220px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#F37626" d="M12 2l8 5-8 5-8-5z"></path></svg>
      <div>
        <strong>Jupyter</strong><br><small>Notebook e documentação</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">Interface para experimentação e apresentação</p>
  </div>

  <!-- Card Alpha Vantage -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:320px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#2E7D32" d="M12 2a10 10 0 100 20 10 10 0 000-20z"></path></svg>
      <div>
        <strong>Alpha Vantage</strong><br><small>Extração de dados financeiros</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">
      Documentação: <a href="https://www.alphavantage.co/documentation/" target="_blank">https://www.alphavantage.co/documentation/</a>
    </p>
  </div>

  <!-- Card Gemini -->
  <div style="border-radius:8px; padding:12px; border:1px solid #e6e6e6; width:320px;">
    <div style="display:flex; align-items:center; gap:10px;">
      <svg width="28" height="28" viewBox="0 0 24 24"><path fill="#DB4437" d="M12 2l4 8h8l-6 6 2 8-8-6-8 6 2-8L0 10h8z"></path></svg>
      <div>
        <strong>Gemini (Google)</strong><br><small>Motor de IA para análise</small>
      </div>
    </div>
    <p style="margin:8px 0 0; font-size:13px;">
      Documentação: <a href="https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br" target="_blank">https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br</a>
    </p>
  </div>
</div>


---

### 1.4 Quais são os benefícios do projeto?

- Aplicação prática de ETL em dados reais  
- Integração entre mercado financeiro e IA  
- Simulação de um ambiente próximo ao mercado profissional  
- Desenvolvimento de um sistema interativo  
- Projeto ideal para portfólio técnico em Ciência de Dados  

---

## ⚙️ 2. Funcionamento do Sistema

O sistema possui **dois modos de operação**:

---

### 🔹 Modo 1 – Análise Automatizada de Ações

O usuário informa o código de uma ação americana (como AAPL, TSLA, MSFT) e o sistema executa:

1. Extração dos dados via Alpha Vantage  
2. Tratamento e organização dos dados  
3. Envio dos dados para a IA  
4. Retorno de um **resumo estratégico voltado ao longo prazo**

---

### 🔹 Modo 2 – Assistente de Investimentos

O sistema também funciona como um **assistente virtual**, permitindo que o usuário tire dúvidas relacionadas a:

- Investimentos  
- Finanças  
- Ações  
- Economia  

Se a pergunta estiver fora desse tema, o sistema retorna uma mensagem de erro solicitando que o usuário refaça a pergunta dentro do contexto financeiro.

---

## 🧩 2.1 Requisitos para Execução

- Python instalado  
- Acesso à internet  
- Bibliotecas necessárias configuradas  
- Chaves de API válidas  

---

### 2.1.1 Versão do Python Utilizada

✅ **Python 3.10 ou superior**

---

### 2.1.2 Uso das Chaves de API

O projeto exige que o usuário utilize suas próprias chaves gratuitas:

- Alpha Vantage: https://www.alphavantage.co/  
- API de IA: Conforme a plataforma utilizada  

⚠️ As chaves não devem ser publicadas em repositórios públicos.

---

## 🚨 3. Aviso Importante

<div style="background-color:#ffe6e6; padding:15px; border-left:5px solid red;">
⚠️ Este projeto possui <strong>finalidade exclusivamente educacional</strong>.  
<br>⚠️ As análises <strong>não representam recomendação de investimento</strong>.  
<br>⚠️ Todo investimento envolve riscos.
</div>

---
## 🔄 4. Fluxo de Execução

O sistema opera através de um pipeline sequencial orquestrado pelo arquivo principal. Abaixo, detalhamos como os módulos interagem desde a inicialização até a entrega da análise.

### Diagrama de Arquitetura

```mermaid
graph TD
    %% Inicialização e Configuração
    Start([Início: python main.py]) --> Config[config.py: Carrega .env e API Keys]
    Config --> Menu{Menu Principal}
    
    %% Fluxo Opção 1: Análise de Ação
    Menu -->|1. Analisar Ação| Input[/Input: Símbolo da Ação/]
    Input --> Fetch[data_fetcher.py: Busca Dados<br/>na Alpha Vantage]
    
    Fetch -->|Dados OK| Process[processing.py: Calcula<br/>Indicadores SMA/RSI]
    Fetch -->|Erro| Menu
    
    Process --> Vis[visualizer.py: Exibe<br/>Tabela e Gráficos]
    Vis --> AI[ai_services.py: Gera<br/>Parecer com Gemini]
    AI --> Menu
    
    %% Fluxo Opção 2: Chat Financeiro
    Menu -->|2. Assistente Financeiro| ChatInput[/Input: Pergunta do Usuário/]
    ChatInput --> ChatValid[ai_services.py: Valida<br/>Tópico e Responde]
    ChatValid --> Menu
    
    %% Encerramento
    Menu -->|3. Sair| End([Fim])
    
    %% Estilização do Gráfico
    style Start fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff
    style End fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
    style Menu fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff
    style AI fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff
    style ChatValid fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff
    style Fetch fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:#2c3e50
    style Config fill:#34495e,stroke:#2c3e50,stroke-width:2px,color:#fff
    style Input fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff
    style ChatInput fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff
```
**⚠️Observação:** Devido às limitações do plano gratuito da Alpha Vantage, a análise da IA é **exclusivamente voltada ao longo prazo**, evitando interpretações de curtíssimo prazo que exigiriam dados intradiários mais avançados.

---

## 🔄 5. Aplicação do Processo ETL

O coração deste projeto está na aplicação prática do processo **ETL (Extract, Transform, Load)**, que foi estruturado de forma clara, organizada e próxima de um ambiente real de dados no mercado financeiro.

Cada etapa foi pensada para garantir:
- Qualidade dos dados
- Confiabilidade das análises
- Integração eficiente com a Inteligência Artificial

---

### 5.1 Como o processo de extração foi aplicado?

<div style="background-color:#eef2f7; padding:15px; border-radius:10px;">
O núcleo do projeto é a aplicação real do processo <strong>ETL (Extract, Transform, Load)</strong>, garantindo qualidade dos dados, confiabilidade das análises e integração eficiente com IA.
</div>

---

### 5.1.1 Limitações da API Alpha Vantage no Plano Gratuito

A escolha da Alpha Vantage foi feita de forma estratégica para simular um cenário real de restrições de dados no mercado. No plano gratuito, a API apresenta as seguintes limitações:

- ✅ Acesso **apenas a ações americanas**
- ✅ Limite de **25 requisições por dia**
- ✅ Periodicidade limitada para dados em tempo real
- ✅ Restrições em dados intradiários mais avançados

Essas limitações foram um fator decisivo para que a **análise fosse direcionada exclusivamente para estratégias de longo prazo**, garantindo coerência com a qualidade e disponibilidade dos dados.

---

### 5.2 Como o processo de transformação foi desenvolvido?

Após a extração, os dados passam pela etapa mais crítica do projeto: **a transformação dos dados**. Esta fase é essencial para garantir que a IA receba informações limpas, organizadas e confiáveis.

As principais etapas de tratamento foram:

- ✅ Remoção de valores nulos ou inconsistentes  
- ✅ Conversão correta dos tipos de dados (datas, preços, volumes)  
- ✅ Padronização dos nomes das colunas  
- ✅ Organização temporal dos registros  
- ✅ Criação de estruturas adequadas para leitura da IA  
- ✅ Filtragem de períodos relevantes para análise de longo prazo  

#### Por que essa etapa é tão importante?

A Inteligência Artificial depende diretamente da **qualidade dos dados de entrada**. Se os dados estiverem:

- Desorganizados  
- Com tipos incorretos  
- Com ruídos ou valores inválidos  

➡️ A análise final também será comprometida.

Por isso, toda a transformação foi pensada para garantir que a IA consiga **interpretar corretamente o comportamento do ativo ao longo do tempo**, tornando a resposta final mais coerente e confiável.

---

### 5.3 Como os dados foram carregados? Qual foi o resultado obtido?

Após a etapa de transformação, os dados tratados são carregados para a **Inteligência Artificial (Gemini)**, que passa a receber um conjunto de informações estruturadas sobre a ação escolhida pelo usuário.

Nesse carregamento, a IA tem acesso a:

- Histórico de preços  
- Variação ao longo do tempo  
- Tendência geral do ativo  
- Indicadores técnicos calculados a partir dos dados  

Com base nessas informações, a IA gera uma **análise em linguagem natural**, voltada para estratégias de longo prazo, de forma clara e acessível ao usuário.

---

#### 📊 Indicadores abordados durante a análise

Durante a análise, alguns **indicadores técnicos** são utilizados como apoio para interpretar o comportamento da ação. Abaixo está uma explicação simplificada dos principais.

✅ **RSI (Índice de Força Relativa)**

O RSI é um indicador que mede a **força do movimento de alta ou de queda de uma ação** em um determinado período.

De forma simples:
- Ele varia de **0 a 100**
- Indica se um ativo pode estar **sobrecomprado** ou **sobrevendido**

- Quando o RSI está **acima de 70**: geralmente indica que a ação pode estar **sobrecomprada**  
  ✅ Isso significa que muitos investidores compraram recentemente, e o preço pode estar temporariamente alto demais.

- Quando o RSI está **abaixo de 30**: geralmente indica que a ação pode estar **sobrevendida**  
  ✅ Isso significa que muitos investidores venderam, e o preço pode estar temporariamente baixo demais.

No longo prazo, o RSI ajuda a:
- Identificar possíveis pontos de entrada mais seguros  
- Evitar comprar um ativo quando ele já está muito esticado para cima  

---

✅ **Média Móvel**

A média móvel é um indicador utilizado para **suavizar as variações do preço ao longo do tempo**. Em vez de olhar apenas o preço do dia, ela mostra o comportamento médio do ativo em um determinado período.

Ela é muito importante para:
- Identificar a **tendência do ativo**
- Entender se a ação está em um movimento de alta, de queda ou de lateralização

De forma geral:
- Quando o preço está **acima da média móvel**, o ativo tende a estar em uma **tendência de alta**
- Quando o preço está **abaixo da média móvel**, o ativo tende a estar em uma **tendência de queda**

No longo prazo, a média móvel ajuda a:
- Confirmar tendências  
- Evitar decisões precipitadas baseadas em oscilações de curto prazo  

---

A partir dessas informações, a IA consegue:

- Interpretar o momento do ativo  
- Avaliar se ele está esticado para cima ou para baixo  
- Identificar a tendência de longo prazo  
- Gerar um **resumo claro, educacional e útil para o usuário**

Tudo isso é apresentado de forma acessível, mesmo para pessoas que nunca tiveram contato com investimentos antes.

---

## 🎥 6. Demonstração do Projeto

### 6.1 Execução do Programa
https://github.com/user-attachments/assets/d342fd90-2467-4171-b79f-a46c4e4b9e44

### 6.2 Visualizações geradas em conjunto com análise da ação escolhida
![Image](https://github.com/user-attachments/assets/0aff57c1-fd9a-46ab-8a97-be774a46e1dc)

---
## 🚀 7. Guia de Configuração e Execução

Este guia detalha o processo para configurar e executar o Consultor Financeiro AI em sua máquina.

### 7.1 Pré-requisitos Essenciais 💻

Certifique-se de ter o **Python 3** instalado em seu sistema operacional.

---

### 7.2 Preparação do Ambiente

#### A. Criação e Ativação do Ambiente Virtual (Recomendado)

```bash
# Cria o ambiente virtual
python -m venv venv

# Ativação do ambiente (macOS/Linux)
source venv/bin/activate

# Ativação do ambiente (Windows)
venv\Scripts\activate
```

#### B. Instalação das Bibliotecas Necessárias
Instale as dependências externas do projeto com o seguinte comando:

```bash
pip install pandas requests python-dotenv google-genai matplotlib
```

### 7.3 Obtenção e Configuração das Chaves de API 🔑
O sistema requer duas chaves de API.

#### A. Obtenha Suas Chaves
API Alpha Vantage: Obtenha sua chave no site da Alpha Vantage.

API Google Gemini: Obtenha sua chave de API do Gemini no Google AI Studio.

#### B. Criação do Arquivo ```.env```
Crie um arquivo chamado ```.env``` no diretório raiz do projeto e insira as chaves obtidas, substituindo os valores de exemplo:

```bash
# Chave para buscar dados financeiros
API_KEY_ALPHA="SUA_CHAVE_ALPHA_VANTAGE_AQUI"

# Chave para o modelo de IA do Google Gemini
API_KEY_GEMINI="SUA_CHAVE_GEMINI_AQUI"
```

### 7.4 Execução do Sistema ▶️
Com o ambiente ativo e as chaves no lugar, execute o arquivo principal:
```bash
python main.py
```
---

## 📬 Contato

| | | |
| :--- | :--- | :--- |
| **👤 Nome:** | Lucas Pimenta Barretto | |
| **<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" width="24" style="vertical-align:middle; margin-right:8px;"> LinkedIn:** | [linkedin.com/in/lucaspimentabarretto](https://www.linkedin.com/in/lucaspimentabarretto) | |
| **📧 Email:** | lucaspimenta1805@gmail.com | |
| **💼 Portfólio**  | [Data Science Portfolio](https://www.datascienceportfol.io/lucaspimenta1805) |

---

<div align="center">
  <h3>📌 Projeto desenvolvido no contexto do bootcamp "Santander 2025 - Ciência de Dados com Python"</h3>
  <p>DIO + Santander</p>
</div>

