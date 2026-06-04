# =========================================================
# Script: 03_process_bitcoin_dataset.py
# Objetivo: Transformar dataset bruto de Bitcoin em formato estruturado
# Camada: PROCESSED (data/processed/)


import pandas as pd
import json
import os

# ---------------------------------------------------------
# Garantia de estrutura de pastas

# Cria diretório de saída caso não exista
os.makedirs("Satoshi_AI/data/processed", exist_ok=True)


# ---------------------------------------------------------
# Carregamento do dataset bruto

# Lê o dataset já exportado na camada RAW
df = pd.read_json("Satoshi_AI/data/raw/bitcoin_dataset.json")


# ---------------------------------------------------------
# Transformação / limpeza do dataset

# Lista que armazenará os dados estruturados
bitcoin_clean = []

# Percorre cada linha do dataset bruto
for _, row in df.iterrows():
    bitcoin_clean.append({
        "topic": "bitcoin_basic",     # categoria fixa do dataset
        "content": row.get("text", "")  # conteúdo principal do texto
    })


# ---------------------------------------------------------
# Exportação do dataset processado

# Salva versão limpa/estruturada para uso em IA/treinamento
with open(
    "Satoshi_AI/data/processed/bitcoin_knowledge.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(bitcoin_clean, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------
# Finalização
# ---------------------------------------------------------

print("Dataset processado com sucesso!")
