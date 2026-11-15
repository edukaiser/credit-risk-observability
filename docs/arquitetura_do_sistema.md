# 🏛️ Arquitetura do Sistema — Credit Risk Observability MLOps

Este documento descreve a arquitetura técnica, o fluxo de dados, a camada de monitoramento e as diretrizes de governança implementadas na **Fase 4 do Tech Challenge da FIAP (Pós-Tech MLOps)**.

---

## 1. Visão Geral da Solução

O projeto foi concebido para mitigar o risco de **degradação silenciosa de modelos de crédito** em produção. A solução atua como uma camada robusta de **Sustentação, Confiabilidade e Observabilidade**, garantindo que anomalias de dados sejam interceptadas, desvios estatísticos (*data drift*) sejam monitorados em tempo real, e todas as execuções sejam auditadas de forma centralizada.

---

## 2. Camadas da Arquitetura

A arquitetura do sistema é dividida em quatro camadas principais:

```text
[ 1. Ingestão & Dados ] ---> [ 2. Validação & Contratos ] ---> [ 3. Simulação & Drift (Evidently) ] ---> [ 4. Observabilidade & Tracking (MLflow) ]
```

### Camada 1: Ingestão e Armazenamento de Dados
* **Dataset de Referência (`data/reference/`)**: Contém os dados históricos limpos utilizados originalmente no treinamento do modelo de *credit scoring*. Serve como baseline estatístico.
* **Dataset de Produção (`data/production/`)**: Simula a chegada de novos dados ao longo do tempo, introduzindo alterações propositais de distribuição (ex: desvios em renda, idade e comportamento de crédito) para testar a resiliência do sistema.

### Camada 2: Validação de Dados e Contratos
* Responsável por assegurar que dados corrompidos ou fora dos padrões de negócio não ingressem no pipeline.
* Aplicação de regras rígidas (tipos de dados, ausência de nulos em colunas obrigatórias, faixas válidas de renda e idade).

### Camada 3: Análise de Drift e Estatística
* Utilização da biblioteca **Evidently AI** para comparar o dataset de referência com o dataset de produção.
* Execução de testes estatísticos automatizados (como Kolmogorov-Smirnov e PSI) para identificar quais *features* sofreram desvio de distribuição.
* Geração automática de relatórios visuais interativos (`reports/data_drift_report.html`).

### Camada 4: Observabilidade e Rastreamento (MLflow)
* Centralização dos logs de execução do pipeline de monitoramento.
* Configuração do **MLflow** com persistência em banco **SQLite (`mlflow.db`)**, eliminando erros comuns de concorrência e File Store.
* Registro de métricas e parâmetros operacionais essenciais:
  * `pipeline_execution_status` (Status de sucesso/falha)
  * `total_tests_executed` (Total de testes estatísticos rodados)
  * `success_tests_count` (Testes aprovados)
  * `failed_tests_count` (Testes reprovados / com drift)
  * `drift_share_ratio` (Proporção de drift detectada)
* Anexação automática do relatório HTML do Evidently como artefato rastreado para fins de auditoria.

---

## 3. Fluxo de Execução dos Notebooks

O pipeline operacional está estruturado em notebooks sequenciais dentro de `notebooks/`:

1. **`01_eda.ipynb`**: Análise exploratória inicial e consolidação do baseline de dados.
2. **`02_drift_analysis.ipynb`**: Configuração das suítes de teste de drift e geração preliminar de indicadores.
3. **`03_observability.ipynb`**: Orquestração final integrando a execução do Evidently com o tracking automatizado no MLflow.

---

## 4. Governança e Conformidade (LGPD)

A arquitetura respeita os princípios de *Privacy by Design* e *Privacy by Default*:
* **Minimização de PII:** Atributos de identificação direta (nomes, CPFs, e-mails) são excluídos ou pseudonimizados.
* **Base Legal:** Operações fundamentadas na Execução de Contrato e Proteção ao Crédito (Art. 7º, V e IX/X da LGPD).
* **Auditabilidade:** Rastreabilidade completa no MLflow permitindo explicar qualquer alteração no comportamento de crédito.

---

## 5. Stack Tecnológica de Suporte

* **Linguagem:** Python 3.12
* **Gerenciamento de Ambiente:** `uv` (`env_credit`)
* **Tracking & Artifacts:** MLflow + SQLite
* **Validação Estatística:** Evidently AI
* **Versionamento:** Git & GitHub (`feat/observability` ➔ `main`)