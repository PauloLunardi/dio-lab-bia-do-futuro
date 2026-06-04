# =========================================================
# Script: 00_run_streamlit_ollama_app.sh
# Objetivo: Instalar dependências, verificar Ollama e rodar aplicação Streamlit
# Camada: SETUP / APPLICATION LAUNCH
# =========================================================


# ---------------------------------------------------------
# 1. Instalação de dependências do projeto
# ---------------------------------------------------------

# Instalação manual (modo direto)
pip install streamlit ollama pandas

# Alternativa via requirements.txt (modo recomendado em produção)
# pip install -r requirements.txt


# ---------------------------------------------------------
# 2. Verificação de modelos no Ollama
# ---------------------------------------------------------

# Lista modelos já instalados localmente
ollama list


# ---------------------------------------------------------
# 3. Inicialização do serviço Ollama
# ---------------------------------------------------------

# Inicia o servidor local do Ollama (necessário para inferência)
ollama serve


# ---------------------------------------------------------
# 4. Execução da aplicação Streamlit
# ---------------------------------------------------------

# Inicia a interface web da aplicação
streamlit run src/app.py
