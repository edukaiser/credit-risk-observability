![Descrição da imagem](docs/img/mlops_banner.png)

# 🩺 Credit Risk Observability MLOps
Projeto de Machine Learning Ops para monitoramento, observabilidade e governança de modelos de concessão e risco de crédito.

---

Resumo rápido (Vídeo Explicativo): [Vídeo S.T.A.R do Projeto](https://seu-link-do-drive-aqui.com)

---

🎯 **Visão Geral**
Este repositório implementa um pipeline completo de MLOps voltado para o monitoramento contínuo de modelos de crédito, análise de desvio de dados (*data drift*) e governança algorítmica. A solução foi concebida para:
- gerenciar e versionar dados e artefatos de referência e produção;
- automatizar a execução de testes de integridade e qualidade de dados com Evidently;
- rastrear experimentos, parâmetros e métricas operacionais centralmente via MLflow;
- prover uma estrutura robusta para auditoria e conformidade com a LGPD;
- assegurar reprodutibilidade de código por meio de práticas modernas de desenvolvimento em Python.

---

👥 **Integrante:** Eduardo Marafigo Kaiser | RM370237

---

🏁 **Objetivo do Projeto**
O objetivo principal do sistema é garantir a observabilidade de modelos e regras de concessão de crédito em ambiente de produção, monitorando ativamente o comportamento das variáveis de entrada, a estabilidade das distribuições estatísticas e a integridade operacional do pipeline de dados.

---

🏛️ **Arquitetura**
A arquitetura do projeto foi estruturada em camadas bem definidas:
- ingestão e armazenamento de dados históricos e de produção;
- suíte de testes de validação e detecção de *data drift*;
- tracking de métricas e registro de artefatos com MLflow (suporte a SQLite);
- documentação arquitetural e de governança focada em privacidade e explicabilidade.

---

🛠️ **Stack Tecnológica**
- 🐍 Python 3.12
- 📦 Gerenciamento de pacotes: `uv`
- 📊 MLflow (com backend SQLite)
- 📈 Evidently AI (para análise de *data drift* e testes estatísticos)
- 🐼 pandas / numpy
- 🧪 pytest / Ruff

---

📂 **Estrutura do Repositório**
```text
credit-risk-observability/
├── data/
│   ├── reference/
│   │   └── reference_data.csv
│   └── production/
│       └── production_data.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_drift_analysis.ipynb
│   └── 03_observability.ipynb
├── reports/
│   └── data_drift_report.html
├── src/
│   └── (módulos utilitários e de pipeline)
├── mlruns/
├── mlflow.db
├── pyproject.toml
└── README.md
```
---

🔄 **Pipeline de ML & Observabilidade**
O pipeline segue uma lógica estruturada de monitoramento:
    1. Carregamento dos datasets de referência (histórico) e produção (simulação atual);
    2. Execução de testes automatizados de estabilidade e drift via Evidently;
    3. Registro centralizado de métricas operacionais no MLflow (total_tests_executed, failed_tests_count, drift_share_ratio, pipeline_execution_status);
    4. Anexação automática de relatórios visuais em HTML como artefatos de auditoria.

---

⚙️ **Como Rodar o Projeto**

1. Clonar o repositório:
```bash
git clone [https://github.com/edukaiser/credit-risk-observability.git](https://github.com/edukaiser/credit-risk-observability.git)
cd credit-risk-observability
```

2. Subir a Interface do MLflow

```bash
$env:MLFLOW_ALLOW_FILE_STORE="true"
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Acesse a interface em http://127.0.0.1:5000.

---

🛡️ **Governança, Privacidade e LGPD (Privacy by Design & By Default)**
Em conformidade com a Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018), o sistema adota as seguintes diretrizes:
Minimização e Anonimização de PII: Atributos de identificação direta são excluídos ou mascarados, focando estritamente em variáveis de risco financeiro e comportamental.
Base Legal para Decisão: Amparado na Execução de Contrato (Art. 7º, V) e Proteção ao Crédito / Legítimo Interesse (Art. 7º, IX e X).
Auditabilidade e Explicabilidade: O uso de rastreamento com MLflow e relatórios de drift assegura que variações na concessão de crédito sejam totalmente auditáveis.

---

🗺️ **Roadmap e Próximos Passos**
Consolidar automações de CI/CD para validação contínua de modelos.
Expandir o monitoramento para métricas de performance de negócio a longo prazo.