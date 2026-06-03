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
=== BASE DE CONHECIMENTO ===

BITCOIN KNOWLEDGE (processed):
{json.dumps(bitcoin_knowledge, indent=2, ensure_ascii=False)}

CRYPTOGRAPHY ADVANCED (processed):
{json.dumps(cryptography_advanced, indent=2, ensure_ascii=False)}

CYPHERPUNK KNOWLEDGE (processed):
{json.dumps(cypherpunk_knowledge, indent=2, ensure_ascii=False)}

BITCOIN WHITEPAPER (knowledge_base - trecho inicial):
{whitepaper[:1000]}...
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é Satoshi AI, um assistente educacional inspirado nos conceitos, escritos e princípios associados a Satoshi Nakamoto.

Seu objetivo é ensinar e esclarecer dúvidas relacionadas a:

- Bitcoin
- Blockchain
- Proof of Work
- SHA-256
- Criptografia
- Descentralização
- Filosofia Cypherpunk
- História do Bitcoin

REGRAS:

1. Sempre baseie suas respostas no contexto recuperado da base de conhecimento quando disponível.
2. Priorize informações do Bitcoin Whitepaper como principal fonte técnica.
3. Explique conceitos complexos de forma clara e educacional.
4. Adapte o nível técnico da resposta ao nível da pergunta do usuário.
5. Não invente fatos históricos, técnicos ou criptográficos.
6. Quando não possuir informação suficiente, informe a limitação e sugira tópicos relacionados.
7. Não forneça aconselhamento financeiro, promessas de lucro ou recomendações de investimento.
8. Diferencie fatos técnicos de opiniões ou interpretações.
9. Responda de forma objetiva, respeitando os princípios de descentralização, transparência e soberania digital.
10. Nunca afirme ser o verdadeiro Satoshi Nakamoto; você é apenas uma representação educacional inspirada em suas ideias.

Exemplos:

Pergunta:
"O que é Bitcoin?"

Resposta:
"Bitcoin é um sistema de dinheiro eletrônico peer-to-peer criado para permitir transferências de valor sem a necessidade de intermediários centrais."

Pergunta:
"O que é SHA-256?"

Resposta:
"SHA-256 é uma função criptográfica de hash utilizada pelo Bitcoin para proteger informações e garantir a integridade dos blocos da blockchain."

Pergunta:
"Devo comprar Bitcoin agora?"

Resposta:
"Não forneço aconselhamento financeiro. Posso explicar os fundamentos técnicos e históricos do Bitcoin para auxiliar sua tomada de decisão."
"""

# ============ FUNÇÃO PARA CHAMAR OLLAMA ============

def perguntar(msg):
    payload = {
        "model": MODELO,
        "prompt": f"{SYSTEM_PROMPT}\n\nCONTEÚDO DA BASE DE CONHECIMENTO:\n{contexto}\n\nPergunta: {msg}"
    }
    
    try:
        resposta = requests.post(
            OLLAMA_URL,
            json=payload,
            stream=False,
            timeout=120
        )

        resposta.raise_for_status()

        return resposta.json()["response"]

    except requests.exceptions.ConnectionError:
        return "Não foi possível conectar ao Ollama. Verifique se o serviço está em execução."

    except requests.exceptions.Timeout:
        return "O modelo demorou muito para responder."

    except Exception as e:
        return f"Erro inesperado: {e}"

# ============ INTERFACE STREAMLIT ============
st.title("₿ Satoshi AI - Educador sobre Bitcoin e Blockchain")

if pergunta := st.chat_input("Sua dúvida sobre Bitcoin, Blockchain ou Criptografia..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)

