# =========================================================
# Script: 02_export_raw_datasets.py
# Objetivo: Converter datasets HuggingFace para JSON bruto
# Local: Satoshi_AI/data/raw/


import os

# Garante que a pasta de saída existe antes de salvar os arquivos
os.makedirs("Satoshi_AI/data/raw", exist_ok=True)


# ---------------------------------------------------------
# Dataset: Bitcoin


# Converte o split "train" do dataset para DataFrame Pandas
df_bitcoin = bitcoin_dataset["train"].to_pandas()

# Salva o dataset em JSON bruto (formato record-by-record)
df_bitcoin.to_json(
    "Satoshi_AI/data/raw/bitcoin_dataset.json",
    orient="records",   # cada linha vira um objeto JSON
    force_ascii=False,  # mantém caracteres especiais (ex: acentos)
    indent=2            # formatação legível (debug e inspeção)
)


# ---------------------------------------------------------
# Dataset: Celestia

# Conversão do dataset Celestia para DataFrame
df_celestia = celestia_dataset["train"].to_pandas()

# Exportação para JSON bruto (sem indentação para menor arquivo)
df_celestia.to_json(
    "Satoshi_AI/data/raw/celestia_dataset.json",
    orient="records",
    force_ascii=False
)


# ---------------------------------------------------------
# Dataset: SHA256 - Bounded

# Converte dataset de testes controlados (bounded)
df_bounded = sha256_bounded["train"].to_pandas()

# Salva versão bruta do dataset
df_bounded.to_json(
    "Satoshi_AI/data/raw/sha256_bounded.json",
    orient="records",
    force_ascii=False
)


# ---------------------------------------------------------
# Dataset: SHA256 - Dynamics

# Dataset com variações dinâmicas de entrada/saída SHA-256
df_dynamics = sha256_dynamics["train"].to_pandas()

# Exportação para camada raw
df_dynamics.to_json(
    "Satoshi_AI/data/raw/sha256_dynamics.json",
    orient="records",
    force_ascii=False
)


# ---------------------------------------------------------
# Dataset: SHA256 - Probe

# Dataset de testes exploratórios (probe cases)
df_probe = sha256_probe["train"].to_pandas()

# Salvando dataset bruto para análise posterior
df_probe.to_json(
    "Satoshi_AI/data/raw/sha256_probe.json",
    orient="records",
    force_ascii=False
)
