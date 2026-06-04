# Como Executar o Satoshi AI

## Pré-requisitos

Antes de iniciar a aplicação, certifique-se de possuir:

* Ollama instalado e configurado
* Modelo LLM baixado localmente (GPT-OSS ou Qwen3)
* Ambiente Powershell instalado
* Estrutura do projeto configurada
---

## 1. Abrir o terminal PowerShell
Abra o **PowerShell** no Windows e navegue até a pasta do projeto:
```powershell
cd C:\Users\lunar\Documents\Satoshi_AI
```
---

## 2. Criar o ambiente virtual (primeira execução)
```powershell
py -3.12 -m venv venv
```

---

## 3. Ativar o ambiente virtual
```powershell
venv\Scripts\activate
```
Após a ativação, o terminal deverá exibir algo semelhante a:

```powershell
(venv) PS C:\Users\lunar\Documents\Satoshi_AI>

```
---

## 4. Instalar as dependências

### Modo 1 - Instalação manual
```powershell
pip install streamlit requests pandas #(não uso pandas no codigo)
pip install requests streamlit
```

### Modo 2 - Arquivo requirements.txt
```powershell
 pip install -r requirements.txt
```
---

## 5. Verificar a instalação

Verificar Python:
```bash
python --version
```

Verificar Pip:
```bash
python -m pip --version
```

Verificar Streamlit:
```bash
streamlit --version
```

---

## 6. Verificar o Ollama

Em um terminal Windows (CMD ou PowerShell):
```bash
ollama list
```

Exemplo:
```text
NAME
qwen3:4b
```

Caso o serviço não esteja ativo:
```bash
ollama serve
```

Verificar modelos carregados(ativos):
```bash
ollama ps
```

---

## 7. Teste e Comunicação com Ollama

No terminal:
```bash
ollama run qwen3:4b "Hello World"
```

```bash
ollama run qwen3:4b "O que é Bitcoin?"
```

Resposta esperada:

```text
Explicação sobre Bitcoin e sistema peer-to-peer.
```
---

## 8. Executar a aplicação

Dentro da pasta do projeto:
```bash
streamlit run src/app.py
```

ou

```bash
python -m streamlit run src/app.py
```
---

## 9. Acessar a interface

Após a execução, o Streamlit disponibilizará um endereço local semelhante a:

```text
http://localhost:8501
```
Abra o endereço no navegador para utilizar o Satoshi AI.

Se preferir pode rodar localmentente:
```powershell
curl http://localhost:11434/api/generate -d "{\"model\": \"qwen3:4b\", \"prompt\": \"Olá, bem-vindo ao Satoshi AI!\"}"
```
---

## 10. Teste e Consulta Básica

Pergunta:
```text
O que é Bitcoin?
```

Resultado esperado:
```text
Explicação introdutória baseada na base de conhecimento.
```

---

## Teste 4 - Consulta Técnica

Pergunta:
```text
Qual é o papel do SHA-256 na blockchain?
```

Resultado esperado:
```text
Explicação técnica sobre hashing, mineração e integridade dos blocos.
```

---

## Teste 5 - Fora do Escopo

Pergunta:
```text
Quem venceu a Copa do Mundo de 2022?
```

Resultado esperado:
```text
O agente informa que é especializado em Bitcoin, blockchain, criptografia e filosofia cypherpunk.
```
