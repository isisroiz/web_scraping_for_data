# 🏦 Projeto de Análise de Câmbio: Almeida LTDA & Banco Central do Brasil

[cite_start]Este projeto implementa uma solução de Engenharia de Dados e Análise em Python para atender aos requisitos da Almeida LTDA, conforme detalhado no **CASE-EDUMI 2022**[cite: 1].

[cite_start]O objetivo é automatizar a aquisição, unificação e tratamento dos dados de Ranking de Câmbio do Banco Central do Brasil (BACEN), fornecendo métricas para a tomada de decisão sobre operações cambiais[cite: 5, 7].

## 🛠️ Tecnologias Utilizadas

* [cite_start]**Python:** Linguagem principal para automação[cite: 23].
* [cite_start]**Pandas:** Essencial para manipulação, unificação e análise dos dados[cite: 44, 51].
* [cite_start]**Requests & Zipfile:** Utilizados para a requisição HTTP e extração de arquivos ZIP diretamente do site do BACEN[cite: 23, 38].
* [cite_start]**Módulos Próprios (`new_lib.py`):** Arquitetura organizada em módulos (biblioteca própria) para garantir a reutilização e limpeza do código (requisito do Case)[cite: 23].

## 📊 Estrutura do Projeto

[cite_start]O projeto é dividido em três fases metodológicas (Aquisição, Tratamento e Análise)[cite: 36, 44, 50].

| Arquivo/Pasta | Descrição |
| :--- | :--- |
| `main.py` | Script principal. Responsável por orquestrar a execução das fases, controlar o laço de repetição (`for`) e iniciar a análise final. |
| `new_lib.py` | Módulo (biblioteca própria) com funções utilitárias: `criar_pasta`, `baixar_e_extrair_zip`, `unificar_bases`, `tratar_dados`, etc. |
| `dados/` | Pasta de saída. Armazena os arquivos CSV baixados do BACEN (`zipfiles/`) e, futuramente, o `base_consolidada_final.csv`. |

## 🚀 Como Executar o Projeto

1.  **Pré-requisitos:** Certifique-se de ter o Python (com Spyder ou seu ambiente de preferência) e as bibliotecas `pandas` e `requests` instaladas.
2.  **Configuração de Caminho:** O script `main.py` utiliza caminhos absolutos (`C:\Users\Isis\...`). Altere as variáveis `DESTINO_BASE` no `main.py` para o caminho local da sua máquina.
3.  **Execução:** Execute o arquivo `main.py`.

## ⚙️ Funcionalidades Automatizadas

A implementação do projeto inclui:

1.  [cite_start]**Criação Estrutural de Pastas:** Garante que a estrutura `dados/` e `dados/zipfiles/` exista[cite: 43].
2.  [cite_start]**Automação Híbrida de Download:** Utiliza a lógica de laço de repetição (`for`) para baixar os dados de 2015 a 2025 (padrões `[MM]-IF-` e `[MM]-[MM]`) e trata a inconsistência do BACEN[cite: 38].
3.  [cite_start]**Unificação Inteligente:** Lê **todos** os arquivos CSV extraídos, aplica correções essenciais (`header=4`, `encoding='latin1'`) e concatena-os em um único DataFrame[cite: 44, 51].

---
[cite_start]*Próximos passos após a aquisição: Finalizar o tratamento (`nl.tratar_dados`) e iniciar a análise das 9 perguntas do case[cite: 9].*
