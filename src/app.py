import json
import pandas as pd
import streamlit as st
import requests

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============

with open("data/processed/bitcoin_knowledge.json", "r", encoding="utf-8") as f:
    bitcoin_knowledge = json.load(f)

with open("data/processed/cryptography_advanced.json", "r", encoding="utf-8") as f:
    cryptography_advanced = json.load(f)

with open("data/processed/cypherpunk_knowledge.json", "r", encoding="utf-8") as f:
    cypherpunk_knowledge = json.load(f)

with open("data/knowledge_base/bitcoin_whitepaper.txt", "r", encoding="utf-8") as f:
    whitepaper = f.read()

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, diga: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ============ FUNÇÃO PARA CHAMAR OLLAMA ============
def perguntar(msg):
    payload = {
        "model": MODELO,
        "prompt": f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"
    }
    resposta = requests.post(OLLAMA_URL, json=payload, stream=False)
    return resposta.json()["response"]

# ============ INTERFACE STREAMLIT ============
st.title("🧠 Edu, o Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
