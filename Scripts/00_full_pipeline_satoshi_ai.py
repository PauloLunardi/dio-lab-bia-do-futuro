# =========================================================
# Script: 00_full_pipeline_satoshi_ai.py
# Objetivo: Pipeline completo (RAW → PROCESSADO) do Satoshi_AI
# Camada: END-TO-END DATA ENGINEERING PIPELINE
# =========================================================

import os
import json
import pandas as pd
from datasets import load_dataset


# =========================
# 1. CRIAÇÃO DA ESTRUTURA DE PASTAS
# =========================

# Diretório base do projeto
BASE_DIR = "Satoshi_AI"

# Pastas de dados
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

# Criação das pastas caso não existam
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

print("Pastas criadas com sucesso.")


# =========================
# 2. CARREGAMENTO DOS DATASETS
# =========================

# Dataset sobre Bitcoin
bitcoin_dataset = load_dataset("Gopher-Lab/bankless_DEBRIEF_-_What_is_Bitcoin")

# Dataset sobre Celestia / filosofia cypherpunk
celestia_dataset = load_dataset(
    "Gopher-Lab/laurashin_How_Satoshi_Nakamoto_and_Vitalik_Buterin_Inspired_Key_Parts_of_Celestia_-_Ep__672"
)

# Dataset de aprendizado de SHA-256 (variações)
sha256_bounded = load_dataset("bshepp/round-reduced-sha256-learnability", "bounded_null")
sha256_dynamics = load_dataset("bshepp/round-reduced-sha256-learnability", "dynamics_validated")
sha256_probe = load_dataset("bshepp/round-reduced-sha256-learnability", "feature_probe")


# =========================
# 3. SALVAMENTO DOS DADOS BRUTOS (RAW LAYER)
# =========================

# Função para salvar datasets em JSON bruto
def save_raw(df, name):
    path = os.path.join(RAW_DIR, f"{name}.json")
    df.to_json(path, orient="records", force_ascii=False, indent=2)
    print(f"Salvo RAW: {path}")


# Conversão para DataFrame
df_bitcoin = bitcoin_dataset["train"].to_pandas()
df_celestia = celestia_dataset["train"].to_pandas()
df_bounded = sha256_bounded["train"].to_pandas()
df_dynamics = sha256_dynamics["train"].to_pandas()
df_probe = sha256_probe["train"].to_pandas()


# Salvamento camada RAW
save_raw(df_bitcoin, "bitcoin_dataset")
save_raw(df_celestia, "celestia_dataset")
save_raw(df_bounded, "sha256_bounded")
save_raw(df_dynamics, "sha256_dynamics")
save_raw(df_probe, "sha256_probe")


# =========================
# 4. PROCESSAMENTO (DATASET PARA IA)
# =========================

# Função de padronização para formato de IA
def process_dataset(df, topic):
    data = []

    for _, row in df.iterrows():

        # tenta extrair campo principal "text"
        text = row.get("text", "")

        # fallback caso não exista coluna estruturada
        if text == "":
            text = str(row.to_dict())

        # estrutura padrão para IA / RAG
        data.append({
            "topic": topic,
            "content": text
        })

    return data


# Construção dos datasets processados
bitcoin_clean = process_dataset(df_bitcoin, "bitcoin_basic")
celestia_clean = process_dataset(df_celestia, "cypherpunk_philosophy")
sha256_clean = process_dataset(df_bounded, "cryptography_advanced")


# =========================
# 5. SALVAMENTO DOS DADOS PROCESSADOS
# =========================

# Função para salvar JSON processado
def save_processed(data, name):
    path = os.path.join(PROCESSED_DIR, f"{name}.json")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Salvo PROCESSADO: {path}")


# Export final da camada PROCESSADA
save_processed(bitcoin_clean, "bitcoin_knowledge")
save_processed(celestia_clean, "cypherpunk_knowledge")
save_processed(sha256_clean, "cryptography_advanced")


# =========================
# FINALIZAÇÃO DO PIPELINE
# =========================

print("PIPELINE FINALIZADO COM SUCESSO 🚀")
