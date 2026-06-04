# ============================================================
# setup inicial obrigatório antes de rodar qualquer script

# Esse bloco garante que a estrutura de diretórios exista
# antes de salvar datasets, embeddings ou qualquer saída do projeto

import os


# ============================================================
# estrutura base do projeto Satoshi AI
# Aqui estamos criando a pasta raiz "Satoshi_AI" e suas subpastas
# para armazenar dados brutos e dados processados

os.makedirs("Satoshi_AI/data/raw", exist_ok=True)
os.makedirs("Satoshi_AI/data/processed", exist_ok=True)


# ============================================================
# observação importante
# exist_ok=True evita erro caso as pastas já existam
# isso é essencial para rodar o script várias vezes (Colab / pipeline)
