"""Script de teste para demonstrar a falha e o bloqueio do contrato Pandera."""

from pathlib import Path

import pandas as pd
import pandera.errors

from src.data.validate_data import validate_dataset


def run_failure_test() -> None:
    """Executa o teste de ingestão com dados inválidos para validar o bloqueio."""
    print("[INFO] Criando lote de dados com ERROS propositais para teste...")

    invalid_data = pd.DataFrame(
        {
            "Age": [-5, 25, 45, 999],
            "Job": [1, 2, 0, 1],
            "Credit amount": [-1000, 1500, 2500, 3000],
            "Duration": [12, 24, 36, 48],
            "Sex": ["male", "female", "invalid_sex", "male"],
            "Housing": ["own", "rent", "own", "free"],
            "Saving accounts": ["little", "moderate", "rich", "unknown"],
            "Checking account": ["little", "moderate", "rich", "bad"],
            "Purpose": ["radio/tv", "education", "furniture", "car"],
            "target": [0, 1, 0, 1],
        }
    )

    # Salva temporariamente os dados sujos para a função ler via caminho
    temp_file = Path("data/raw/invalid_test_data.csv")
    temp_file.parent.mkdir(parents=True, exist_ok=True)
    invalid_data.to_csv(temp_file, index=False)

    print("[INFO] Tentando executar a validação com o arquivo sujo...")
    try:
        validate_dataset(temp_file)
        print("[ALERTA] O contrato NÃO bloqueou os dados! Algo está errado.")
    except (pandera.errors.SchemaError, pandera.errors.SchemaErrors) as err:
        print("\n[SUCESSO] O contrato do Pandera FUNCIONOU e bloqueou a ingestão!")
        print(f"Detalhes do erro capturado:\n{err}")
    finally:
        # Limpa o arquivo temporário depois do teste
        if temp_file.exists():
            temp_file.unlink()


if __name__ == "__main__":
    run_failure_test()