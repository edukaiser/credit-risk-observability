# 📋 Tech Challenge — Fase 4: Especificação Oficial e Escopo do Projeto

**Pós-Tech MLOps (FIAP)**  
**Tema Central:** Observabilidade Contínua, Detecção de Drift, Qualidade de Dados e Governança em Produção.

---

## 🎯 1. Contexto do Projeto
Uma fintech de concessão de crédito possui um modelo de *Credit Scoring* em produção. Devido a recentes flutuações macroeconômicas (inflação, juros e novos perfis de clientes), há suspeita de degradação silenciosa do modelo e tomada de decisões incorretas. 

O objetivo deste projeto é construir a **camada de Sustentação e Confiabilidade**, implementando validação de dados na entrada, simulação e detecção de *Data/Concept Drift*, observabilidade centralizada de pipelines e governança sob os princípios da LGPD.

---

## 🏗️ 2. Requisitos Obrigatórios e Arquitetura

O projeto foi estruturado para atender rigorosamente aos seguintes entregáveis solicitados pela banca avaliadora:

1. **Repositório GitHub Padronizado:**
   - Histórico de commits semântico e organizado em inglês (`feat`, `chore`, `docs`).
   - Estrutura modular separando dados, notebooks, relatórios e código-fonte.
   - Branch principal (`main`) atualizada com todas as entregas integradas.

2. **Pipeline de Validação de Dados (Data Contracts):**
   - Dataset de Referência limpo e estruturado.
   - Regras rígidas de qualidade (ausência de nulos em campos críticos, faixas válidas de renda e idade, eliminação de duplicatas) para impedir a ingestão de dados corrompidos.

3. **Simulação e Detecção Estatística de Drift:**
   - Criação de um "Dataset de Produção" simulando a alteração proposital de distribuição em variáveis-chave.
   - Utilização do **Evidently AI** para gerar testes estatísticos (PSI, Kolmogorov-Smirnov) e relatórios visuais em HTML apontando as variáveis degradadas.

4. **Observabilidade de Pipelines e Modelos (MLflow):**
   - Centralização de logs operacionais e métricas de execução.
   - Configuração do **MLflow** com backend SQLite (`mlflow.db`) para evitar bloqueios de File Store.
   - Registro de métricas fundamentais: `pipeline_execution_status`, `total_tests_executed`, `success_tests_count`, `failed_tests_count` e `drift_share_ratio`.
   - Anexação automática do relatório HTML do Evidently como artefato rastreado.

5. **Governança, Privacidade e LGPD:**
   - Documentação robusta no `README.md` cobrindo o tratamento de PII (Personally Identifiable Information), minimização de dados, base legal (Art. 7º da LGPD) e plano de retenção.

6. **Vídeo S.T.A.R. (≤ 5 minutos):**
   - Apresentação estruturada cobrindo:
     - **Situation:** O risco da degradação silenciosa de modelos de crédito.
     - **Task:** Requisitos técnicos de interceptação de dados, detecção de drift e compliance.
     - **Action:** Ferramentas escolhidas (Pandera, Evidently, MLflow) e simulação do drift.
     - **Result:** Demonstração prática do relatório de drift, métricas ativas na UI do MLflow e lições aprendidas.

---

## 📊 3. Critérios de Avaliação e Pesos

| Critério de Avaliação | Peso | Descrição do Atendimento no Projeto |
| :--- | :---: | :--- |
| **Validação de Dados** | 25% | Contratos de dados configurados corretamente, garantindo integridade e bloqueando anomalias na entrada. |
| **Detecção de Drift** | 25% | Simulação precisa de alteração de distribuição e geração clara do relatório estatístico com Evidently AI. |
| **Observabilidade e Logs** | 20% | Rastreamento centralizado no MLflow com métricas de saúde do pipeline e alertas de drift documentados. |
| **Governança (LGPD)** | 15% | Clareza na documentação sobre privacidade, minimização de PII, bases legais e mitigação de vieses. |
| **Vídeo S.T.A.R.** | 15% | Apresentação concisa e técnica da degradação do modelo, evidenciando os resultados em produção. |

---

## 🛠️ 4. Stack Tecnológica Utilizada
- **Linguagem:** Python 3.12
- **Gerenciamento de Ambiente:** `uv` / Virtual Environments (`env_credit`)
- **Qualidade de Dados & Contratos:** Pandas, regras de validação estruturadas
- **Detecção de Drift:** Evidently AI
- **Tracking & Observabilidade:** MLflow (com backend SQLite)
- **Versionamento & Repositório:** Git & GitHub
