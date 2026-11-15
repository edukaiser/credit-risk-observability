"""Módulo de Contrato de Dados utilizando Pandera para validação de regras de crédito."""

from pathlib import Path

import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema

# Definição estrita do Contrato de Dados (Data Contract)
credit_schema = DataFrameSchema(
    {
        "Age": Column(int, Check.between(18, 100, error="Idade fora do intervalo permitido (18-100).")),
        "Sex": Column(str, Check.isin(["male", "female"], error="Gênero inválido.")),
        "Job": Column(int, Check.between(0, 3, error="Categoria de Job inválida.")),
        "Housing": Column(str, Check.isin(["own", "rent", "free"], error="Tipo de moradia inválido.")),
        "Saving accounts": Column(str, nullable=True),
        "Checking account": Column(str, nullable=True),
        "Credit amount": Column(float, Check.greater_than(0, error="O valor do crédito deve ser maior que zero.")),
        "Duration": Column(int, Check.greater_than(0, error="A duração do empréstimo deve ser maior que zero.")),
        "Purpose": Column(str),
        "target": Column(int, Check.isin([0, 1], error="Target binário inválido (deve ser 0 ou 1).")),
    },
    strict=True,  # Garante falha caso colunas extras não mapeadas entrem no lote
    coerce=True,   # Tenta converter tipos compatíveis automaticamente
)


def validate_dataset(file_path: str) -> pd.DataFrame:
    """Lê um dataset e aplica o contrato de dados do Pandera, interceptando anomalias."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    df = pd.read_csv(path)

    try:
        validated_df = credit_schema.validate(df, lazy=True)
        print(f"[Sucesso] Contrato validado com sucesso para: {file_path} ({len(validated_df)} linhas)")
        return validated_df
    except pa.errors.SchemaErrors as err:
        print(f"[Erro de Contrato] Falha na validação de qualidade de dados em: {file_path}")
        print(err.failure_cases)
        raise


if __name__ == "__main__":
    # Valida tanto o conjunto de referência quanto o de produção
    print("--- Validando Dataset de Referência ---")
    validate_dataset("data/reference/reference_data.csv")

    print("\n--- Validando Dataset de Produção ---")
    validate_dataset("data/production/production_data.csv")