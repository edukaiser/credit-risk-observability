# 📄 Model Card — Modelo de Risco de Crédito (Credit Scoring)

## 📌 Visão Geral do Modelo
* **Desenvolvedor:** Eduardo Marafigo Kaiser (Pós-Tech MLOps - FIAP)
* **Data da Publicação:** Novembro de 2026
* **Versão do Modelo:** 1.0.0
* **Tipo de Modelo:** Classificador Binário de Risco de Crédito (Previsão de inadimplência / adimplência).
* **Domínio:** Setor Financeiro / Fintech de Crédito.

---

## 🎯 Intenção de Uso e Finalidade
* **Uso Primário:** Auxiliar na tomada de decisão automatizada ou semi-automatizada para concessão de crédito, avaliando a probabilidade de um cliente honrar seus compromissos financeiros.
* **Usuários Alvo:** Analistas de risco de crédito, sistemas automatizados de core bancário e equipes de conformidade e MLOps.
* **Fora de Escopo:** O modelo não deve ser utilizado isoladamente para recusa definitiva de crédito sem possibilidade de revisão humana ou auditoria regulatória.

---

## 📊 Dados Utilizados
* **Dataset de Referência (`reference_data.csv`):** Dados históricos limpos contendo variáveis socioeconômicas, histórico de crédito, renda declarada e pontuação comportamental. Utilizado como baseline para treinamento e testes estáticos.
* **Dataset de Produção (`production_data.csv`):** Dados simulados refletindo cenários de estresse econômico e variações de distribuição (desvios em renda e taxa de desemprego) para monitoramento em tempo real.

---

## 📈 Desempenho e Métricas do Modelo
Durante a fase de validação e rastreamento no MLflow, o modelo e seu pipeline de monitoramento demonstram as seguintes métricas operacionais e estatísticas:
* **Acurácia / Precisão:** Avaliadas no baseline histórico para mitigar falsos positivos na concessão de crédito.
* **Métricas de Observabilidade (Evidently AI + MLflow):**
  * `total_tests_executed`: 4 testes estatísticos principais.
  * `success_tests_count`: Monitoramento de estabilidade por feature.
  * `drift_share_ratio`: Taxa de desvio calculada entre referência e produção (utilizando testes como Kolmogorov-Smirnov e PSI).
  * `pipeline_execution_status`: Status de sucesso operacional (`1`).

---

## 🛡️ Considerações Éticas, Limitações e LGPD
* **Viés e Equidade:** Modelos de crédito baseados em dados históricos podem perpetuar vieses socioeconômicos. É mandatória a auditoria contínua das variáveis de entrada.
* **Privacidade (LGPD):** Atributos de identificação direta (PII) foram estritamente removidos ou pseudonimizados. As decisões automatizadas baseiam-se em legítimo interesse e execução de contrato (Art. 7º, V e IX/X da LGPD).
* **Degradação Silenciosa:** Sujeito a *Data Drift* e *Concept Drift* decorrentes de flutuações macroeconômicas (inflação, desemprego), mitigado pela camada de observabilidade contínua via MLflow e Evidently.

---

## 🔄 Monitoramento e Manutenção
* O modelo é monitorado ativamente por meio de pipelines agendados que geram relatórios de drift em HTML (`reports/data_drift_report.html`) e registram métricas no banco SQLite do MLflow (`mlflow.db`).