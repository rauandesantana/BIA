# BIA (Predictive ETL & AI Engine)

## Visão Geral
A **BIA** é um motor de Inteligência Artificial preditivo construído do zero, focado na análise de dados contínuos e séries temporais. Seu objetivo principal é identificar padrões passados para gerar previsibilidade de resultados futuros, atuando de forma integrada a pipelines de ETL.

## Arquitetura do Projeto
O design do sistema prioriza a robustez através de múltiplas camadas de validação (filtros rigorosos) desde a ingestão dos dados até o treinamento da rede neural.

- **`data/`**: Armazenamento isolado (ignorado pelo Git).
  - `raw/`: Dados brutos extraídos do banco/SQL.
  - `processed/`: Matrizes temporais normalizadas e prontas para a IA.
- **`src/`**: Código-fonte principal.
  - `etl_pipeline/`: Lógica de limpeza, normalização e fatiamento temporal (janelas deslizantes).
  - `model/`: Arquitetura matemática da rede neural.
  - `utils/`: Checagens de sistema e validações de ambiente.
- **`config/`**: Variáveis e hiperparâmetros centralizados (`settings.json`).
- **`logs/`**: Registros de execução e alertas estruturais.

## Configuração do Ambiente Local

Para rodar este projeto, é necessário utilizar um ambiente virtual isolado (`venv`).

1. Ative o ambiente virtual:
   - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
   - Windows (CMD): `.\venv\Scripts\activate.bat`
   - Linux/Mac: `source venv/bin/activate`

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt