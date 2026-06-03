# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar ( vai mudar)

```bash

# 1. Garantir que o Ollama está rodando
ollama serve

# 2. Rodar a aplicação:
python -m streamlit run src/app.py
```

# 📌 Melhorias Futuras - Satoshi AI

Este documento registra ideias e ajustes que podem ser aplicados ao projeto **Satoshi AI** para evoluir sua experiência e desempenho.

---

## 🎭 Personalidade Cypherpunk
- Ajustar o **System Prompt** para reforçar estilo reflexivo e filosófico.
- Instruções adicionais:
  - "Responda como um educador cypherpunk."
  - "Use frases curtas e impactantes sobre liberdade e descentralização."
  - "Adote tom inspirado nos escritos de Satoshi Nakamoto."

---

## ⚡ Modelos Intermediários
- Testar modelos que equilibram **leveza** e **personalidade**:
  - [qwen2.5:7b](ca://s?q=Modelo_qwen2.5_7b) → mais nuance que o 4b, ainda rápido.
  - [llama3:8b](ca://s?q=Modelo_llama3_8b) → bom equilíbrio entre estilo e performance.
  - [mistral:7b](ca://s?q=Modelo_mistral_7b) → eficiente e expressivo, ideal como meio termo.

- Configuração no `app.py`:
  ```python
  OLLAMA_URL = "http://localhost:11434/api/generate"
  MODELO = "mistral:7b"
```
