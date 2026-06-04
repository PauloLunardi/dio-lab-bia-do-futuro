# =========================================================
# Script: 02_build_ia_json_model.py
# Objetivo: Padronizar dataset no formato consumido pela IA
# Camada: DATASET IA / FORMATADO
# =========================================================

import json
import os

# ---------------------------------------------------------
# Garantia de estrutura de diretório
# ---------------------------------------------------------

# Cria pasta base de saída caso não exista
os.makedirs("Satoshi_AI/data", exist_ok=True)


# ---------------------------------------------------------
# Construção do dataset estruturado para IA
# ---------------------------------------------------------

# Lista final no formato padronizado para consumo do modelo
data = []

# Percorre o DataFrame já carregado anteriormente
for _, row in df.iterrows():
    data.append({
        "source": "what_is_bitcoin",   # identifica origem do conhecimento
        "content": row.to_dict(),      # mantém estrutura flexível do registro
    })


# ---------------------------------------------------------
# Exportação do dataset no formato final da IA
# ---------------------------------------------------------

# Salva dataset estruturado pronto para uso em IA/RAG
with open(
    "Satoshi_AI/data/what_is_bitcoin.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
