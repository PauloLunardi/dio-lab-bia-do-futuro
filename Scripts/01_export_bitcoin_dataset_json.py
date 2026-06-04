# =========================================================
# Script: 01_export_bitcoin_dataset_json.py
# Objetivo: Converter dataset Bitcoin (HuggingFace) para JSON bruto
# Camada: RAW / DATA EXPORT
# =========================================================

# ---------------------------------------------------------
# Conversão do dataset para DataFrame
# ---------------------------------------------------------

# Converte o split "train" do dataset para pandas DataFrame
df = bitcoin_dataset["train"].to_pandas()


# ---------------------------------------------------------
# Exportação para JSON
# ---------------------------------------------------------

# Salva o dataset em formato JSON bruto (records)
df.to_json(
    "data/bitcoin_dataset.json",  # caminho de saída
    orient="records",             # cada linha vira um objeto JSON
    force_ascii=False             # mantém caracteres especiais
)
