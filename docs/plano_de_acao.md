# 🗺️ Plano de Ação — Credit Risk Observability MLOps

Este documento detalha o plano de execução, as etapas de desenvolvimento e os marcos (*milestones*) cumpridos durante a realização do **Tech Challenge da Fase 4 da Pós-Tech MLOps (FIAP)**.

## 🎯 Objetivo do Plano
Estabelecer um roteiro estruturado para transformar a necessidade de negócio (mitigação da degradação silenciosa de modelos de crédito) em um pipeline robusto de observabilidade, detecção de drift, qualidade de dados e governança.

---

## 📅 Cronograma de Fases e Marcos

### Etapa 1: Validação de Dados e Contratos (Data Contracts)
* **Objetivo:** Garantir a integridade dos dados de entrada e impedir que dados corrompidos afetem o modelo.
* **Tarefas Executadas:**
  * Estruturação do dataset de referência (`reference_data.csv`) baseado em dados históricos de risco de crédito.
  * Implementação de validações e restrições de schema (tipos de dados, ausência de nulos em colunas críticas, limites de faixa para renda e idade).
  * Criação do notebook exploratório (`01_eda.ipynb`).
* **Status:** ✅ Concluído.

### Etapa 2: Simulação e Detecção Estatística de Drift
* **Objetivo:** Simular o impacto macroeconômico ao longo do tempo e identificar desvios estatísticos (*Data Drift*).
* **Tarefas Executadas:**
  * Criação do dataset de produção (`production_data.csv`) com alterações propositais de distribuição em variáveis-chave.
  * Integração com a biblioteca **Evidently AI** para execução de suítes de teste de estabilidade.
  * Geração do relatório visual automatizado de drift (`reports/data_drift_report.html`).
  * Desenvolvimento do notebook de análise (`02_drift_analysis.ipynb`).
* **Status:** ✅ Concluído.

### Etapa 3: Observabilidade de Pipelines e Modelos (MLflow)
* **Objetivo:** Centralizar logs operacionais, parâmetros e métricas de saúde do pipeline.
* **Tarefas Executadas:**
  * Resolução de erros de concorrência com migração do backend do MLflow para **SQLite (`mlflow.db`)**.
  * Construção do script de rastreamento robusto e blindado no notebook `03_observability.ipynb`.
  * Registro de métricas chave na UI do MLflow:
    * `pipeline_execution_status`
    * `total_tests_executed`
    * `success_tests_count`
    * `failed_tests_count`
    * `drift_share_ratio`
  * Anexação do relatório HTML do Evidently como artefato oficial de auditoria.
* **Status:** ✅ Concluído.

### Etapa 4: Governança, LGPD e Vídeo S.T.A.R.
* **Objetivo:** Garantir conformidade legal, privacidade de dados e apresentação executiva do projeto.
* **Tarefas Executadas:**
  * Elaboração de documentação completa de governança e conformidade com a LGPD no `README.md`.
  * Criação de especificações arquiteturais e técnicas (`docs/tech_challenge_spec.md`, `docs/arquitetura.md`, `docs/action_plan.md`).
  * Gravação e estruturação do vídeo S.T.A.R. demonstrando o cenário, ações, resultados e lições aprendidas.
* **Status:** 🚀 Em finalização.

---

## 🔍 Próximos Passos e Manutenção Contínua
1. **Revisão Final do Repositório:** Validar se todos os arquivos e branches (`feat/observability` e `main`) estão sincronizados no GitHub.
2. **Submissão do Vídeo S.T.A.R.:** Inserir o link oficial de acesso ao vídeo no topo do `README.md`.
3. **Fechamento Oficial:** Validação final perante a rubrica de avaliação da FIAP.