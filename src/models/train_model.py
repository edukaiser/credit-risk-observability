"""Módulo de treinamento do modelo baseline de classificação de risco de crédito."""

from datetime import datetime
import json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def load_and_prepare_data(file_path: str):
    """Carrega os dados e separa features (X) e target (y)."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset de referência não encontrado em: {file_path}")

    df = pd.read_csv(path)
    target_col = "target" if "target" in df.columns else df.columns[-1]
    
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    return X, y


def train_baseline():
    """Executa o pipeline de treinamento do modelo baseline."""
    print("[INFO] Carregando dados de referência...")
    X, y = load_and_prepare_data("data/reference/reference_data.csv")

    # Divisão treino e teste (Holdout)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Adicionado "str" para evitar o aviso de depreciação do Pandas
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_features = X.select_dtypes(include=["object", "str", "category"]).columns.tolist()

    print(f"[INFO] Features numéricas: {numeric_features}")
    print(f"[INFO] Features categóricas: {categorical_features}")

    # Pré-processador e Pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical_features),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )

    print("[INFO] Treinando o modelo baseline...")
    pipeline.fit(X_train, y_train)

    # Avaliação no conjunto de teste
    y_pred = pipeline.predict(X_test)
    y_proba = pipeline.predict_proba(X_test)[:, 1]

    roc_auc = roc_auc_score(y_test, y_proba)
    acc = accuracy_score(y_test, y_pred) 

    print(f"\n[AVALIAÇÃO] ROC-AUC Score: {roc_auc:.4f}")
    print(f"[AVALIAÇÃO] Acurácia: {acc:.4f}")
    print("\n[AVALIAÇÃO] Relatório de Classificação:")
    print(classification_report(y_test, y_pred))

    # --- SALVANDO AS MÉTRICAS EM JSON ---
    metrics_data = {
        "timestamp": datetime.now().isoformat(),
        "model_name": "LogisticRegression",
        "roc_auc": float(roc_auc),
        "accuracy": float(acc),
    }

    metrics_dir = Path("metrics")
    metrics_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = metrics_dir / "metrics.json"

    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_data, f, indent=4, ensure_ascii=False)
    print(f"[SUCESSO] Métricas salvas em formato JSON em: {metrics_path}")

    # --- SALVANDO O ARTEFATO DO MODELO ---
    models_dir = Path("models")
    models_dir.mkdir(parents=True, exist_ok=True)
    model_path = models_dir / "baseline_model.joblib"
    
    joblib.dump(pipeline, model_path)
    print(f"[SUCESSO] Modelo salvo com sucesso em: {model_path}")


if __name__ == "__main__":
    train_baseline()