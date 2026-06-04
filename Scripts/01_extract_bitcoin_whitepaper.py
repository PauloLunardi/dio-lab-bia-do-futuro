# =========================================================
# Script: 01_extract_bitcoin_whitepaper.py
# Objetivo: Extrair texto do Bitcoin Whitepaper em PDF e salvar como TXT
# Camada: RAW / DOCUMENTS PROCESSING
# Ambiente: Google Colab
# =========================================================

import fitz  # PyMuPDF (usado para leitura de PDFs)
from google.colab import files
import os

# ---------------------------------------------------------
# Upload do arquivo PDF
# ---------------------------------------------------------

# Permite upload manual do arquivo no ambiente Colab
uploaded = files.upload()


# ---------------------------------------------------------
# Leitura do PDF
# ---------------------------------------------------------

# Abre o arquivo PDF enviado (Bitcoin Whitepaper)
doc = fitz.open("bitcoin.pdf")

# Variável que armazenará todo o texto extraído
text = ""

# Itera por todas as páginas do PDF e extrai o texto
for page in doc:
    text += page.get_text()


# ---------------------------------------------------------
# Garantia de estrutura de diretório
# ---------------------------------------------------------

# Cria pasta base do projeto caso não exista
os.makedirs("Satoshi_AI", exist_ok=True)


# ---------------------------------------------------------
# Salvamento do conteúdo extraído
# ---------------------------------------------------------

# Salva o texto do whitepaper em formato .txt
with open(
    "Satoshi_AI/bitcoin_whitepaper.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(text)


# ---------------------------------------------------------
# Download do arquivo processado
# ---------------------------------------------------------

# Faz download automático do arquivo gerado
files.download("Satoshi_AI/bitcoin_whitepaper.txt")
