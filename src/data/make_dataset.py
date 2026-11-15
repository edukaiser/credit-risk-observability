"""Módulo de ingestão, limpeza, criação de target sintético e particionamento do dataset German Credit."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


def process_data(raw_path: str, reference_out: str, production_out: str) -> None:
    """Carrega dados brutos, cria o target baseado em regras de crédito, limpa e particiona."""
    Path(reference_out).parent.mkdir(parents=True, exist_ok=True)
    Path(production_out).parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(raw_path)

    # Remove coluna de índice antiga se existir
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Tratamento de nulos nas colunas categóricas
    for col in ("Saving accounts", "Checking account"):
        if col in df.columns:
            df[col] = df[col].fillna("unknown")

    # Criação do target sintético de risco de crédito (1 = mau pagador / alto risco, 0 = bom pagador)
    # Regra: Empréstimos com alta intensidade (Credit amount alto para Duration curta ou valores muito expressivos)
    if "target" not in df.columns:
        # Exemplo de limiar baseado nos quantis do dataset
        high_amount = df["Credit amount"].quantile(0.75)
        high_duration = df["Duration"].quantile(0.75)

        df["target"] = (
            (df["Credit amount"] >= high_amount) | (df["Duration"] >= high_duration)
        ).astype(int)

    # Divisão estratificada entre Dataset de Referência (treino) e Produção (simulação)
    reference_df, production_df = train_test_split(
        df,
        test_size=0.3,
        random_state=42,
        stratify=df["target"],
    )

    reference_df.to_csv(reference_out, index=False)
    production_df.to_csv(production_out, index=False)
    print(
        f"[Sucesso] Target gerado e arquivos salvos:\n - {reference_out}\n - {production_out}"
    )


if __name__ == "__main__":
    RAW_DATA = "data/raw/german_credit_data.csv"
    REF_DATA = "data/reference/reference_data.csv"
    PROD_DATA = "data/production/production_data.csv"

    process_data(RAW_DATA, REF_DATA, PROD_DATA)
