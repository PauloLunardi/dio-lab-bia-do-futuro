# =========================================================
# Script: 00_setup_ollama_models.sh
# Objetivo: Instalar e testar modelos locais via Ollama
# Camada: SETUP / LOCAL LLM ENVIRONMENT
# =========================================================

# ---------------------------------------------------------
# 1. Instalação do Ollama
# ---------------------------------------------------------
# A instalação do Ollama deve ser feita pelo site oficial:
# https://ollama.com
# (não via pip, pois é uma ferramenta nativa do sistema)


# ---------------------------------------------------------
# 2. Baixar modelo leve para testes
# ---------------------------------------------------------

# Faz download do modelo GPT OSS (leve)
ollama pull gpt-oss

# Teste básico de execução do modelo
ollama run gpt-oss "Olá!"


# ---------------------------------------------------------
# 3. Baixar modelo alternativo (Qwen)
# ---------------------------------------------------------

# Download do modelo Qwen 3 versão 4B (mais potente)
ollama pull qwen3:4b

# Teste de execução do modelo Qwen
ollama run qwen3:4b "Olá!"
