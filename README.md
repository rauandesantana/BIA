# BIA (Predictive ETL & AI Engine)

## Visão Geral
A **BIA** é um motor de Inteligência Artificial preditivo e totalmente *stateless* (sem estado/sem persistência de dados locais), focado na análise de dados contínuos e séries temporais em memória. O sistema atua como um cérebro volátil que recebe os fluxos de dados de forma transiente, processa as tarefas utilizando pacotes de conhecimento modular e entrega os resultados sem reter bases de dados em disco.

## Arquitetura do Projeto
O design do sistema prioriza a robustez através de múltiplas camadas de validação e utiliza **Module Packs** para encapsular as regras de negócio e os aprendizados de cada domínio.

- **`config/`**: Variáveis centralizadas, hiperparâmetros e registo de comandos dinâmicos (`settings.json`).
- **`module_packs/`**: O "Cérebro em Módulos" (Pacotes de conhecimento versionados e desacoplados).
  - `etl_core/`: Regras de limpeza, interpolação e normalização temporal.
  - `predictive_engine/`: Arquitetura matemática da rede neural.
- **`src/`**: Código-fonte principal do runtime volátil.
  - `runtime/`: Núcleo de execução em memória.
  - `utils/`: Validações de ambiente e ferramentas de sistema.
- **`logs/`**: Registos operacionais voláteis para observabilidade em tempo de execução (ignorados pelo Git).

## Configuração e Utilização da CLI

A BIA possui um orquestrador universal (`bia.py`) que dispensa a ativação manual de ambientes virtuais para comandos rotineiros.

1. **Ver comandos disponíveis:**
   ```bash
   python bia.py