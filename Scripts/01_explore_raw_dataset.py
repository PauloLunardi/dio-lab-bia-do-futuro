# =========================================================
# Script: 01_explore_raw_dataset.py
# Objetivo: Explorar estrutura do dataset bruto (EDA inicial)
# Camada: RAW (data/raw/)

import pandas as pd

# ---------------------------------------------------------
# Carregamento do dataset bruto

# Lê o dataset JSON já salvo na camada RAW
df = pd.read_json("Satoshi_AI/data/raw/bitcoin_dataset.json")

# ---------------------------------------------------------
# Inspeção da estrutura do dataset

# Exibe os nomes das colunas disponíveis no dataset
print(df.columns)

# Exibe as primeiras linhas para entender o formato dos dados
print(df.head())
