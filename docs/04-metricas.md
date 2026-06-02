# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| Assertividade | O agente respondeu corretamente à pergunta? | Perguntar o que é Bitcoin e receber uma explicação correta |
| Segurança | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir a limitação |
| Coerência | A resposta está alinhada ao Bitcoin Whitepaper e à base de conhecimento? | Explicar Proof of Work sem contradizer as fontes utilizadas |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: 
- **Nível:** Iniciante
- **Pergunta:** "O que é Bitcoin?"
- **Resposta esperada:** Bitcoin é uma moeda digital descentralizada que permite transferências de valor sem intermediários.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```

Resultado: [ ] Correto [ ] Incorreto

### Teste 2:
- **Nível:** Intermediário
- **Pergunta:** "Como funciona a mineração do Bitcoin?"
- **Resposta esperada:** A mineração utiliza o mecanismo Proof of Work para validar blocos e proteger a rede Bitcoin através da resolução de desafios criptográficos.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```

Resultado: [ ] Correto [ ] Incorreto

### Teste 3:
- **Nível:** Técnico
- **Pergunta:** "Qual é o papel do SHA-256 na blockchain do Bitcoin?"
- **Resposta esperada:** O SHA-256 é a função hash utilizada para garantir integridade dos dados, encadear blocos e realizar o processo de mineração do Bitcoin.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```

Resultado: [ ] Correto [ ] Incorreto

### Teste 4: 
- **Nível:** Avançado
- **Pergunta:** "Como o Bitcoin resolve o problema do gasto duplo?"
- **Resposta esperada:** O Bitcoin utiliza blockchain, consenso distribuído e Proof of Work para impedir que uma mesma unidade monetária seja gasta mais de uma vez.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```

Resultado: [ ] Correto [ ] Incorreto

### Teste 5: 
- **Nível:** Challenger
- **Pergunta:** "Por que encontrar um hash válido na mineração do Bitcoin é considerado computacionalmente difícil?"
- **Resposta esperada:** Porque os mineradores precisam realizar inúmeras tentativas alterando o nonce até encontrar um hash SHA-256 abaixo da meta de dificuldade definida pela rede.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```
Resultado: [ ] Correto [ ] Incorreto

### Teste 6:
- **Nível:** Fora de Escopo
- **Pergunta:** "Quem venceu a Copa do Mundo de 2022?"
- **Resposta esperada:** O agente deve informar que é especializado em Bitcoin, blockchain, criptografia e filosofia cypherpunk, não possuindo foco em eventos esportivos.

Resposta do Satoshi AI:
```text
[Preencher após execução]
```

Resposta do ChatGPT:
```text
[Preencher após execução]
```

Resposta do Copilot:
```text
[Preencher após execução]
```

Resposta do Grok:
```text
[Preencher após execução]
```

Resposta do Gemini:
```text
[Preencher após execução]
```

Resultado: [ ] Correto [ ] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
