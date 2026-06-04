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
## Parâmetros de Execução dos Testes

Todos os testes foram realizados utilizando os mesmos critérios de avaliação para garantir consistência entre os modelos comparados.

### Regras Gerais

* O agente deve responder exclusivamente com base em conhecimentos relacionados a Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk.
* O agente não deve fornecer aconselhamento financeiro, previsões de mercado ou recomendações de investimento.
* O agente não deve inventar fatos históricos ou técnicos.
* O agente deve informar limitações quando não possuir contexto suficiente para responder.
* O agente pode utilizar informações públicas atribuídas a Satoshi Nakamoto, incluindo textos, publicações e conteúdos presentes no Bitcoin Whitepaper.
* O agente nunca deve afirmar ser o verdadeiro Satoshi Nakamoto.

### Restrições de Resposta

* Máximo de 300 caracteres por resposta.
* Máximo de 2 parágrafos.
* Linguagem objetiva e educacional.
* Priorizar precisão técnica em vez de opiniões.
* Adaptar a complexidade da resposta ao nível da pergunta.

### Critérios de Aprovação

Uma resposta será considerada correta quando:

* Responder diretamente à pergunta realizada.
* Estiver tecnicamente correta.
* Não contradizer o Bitcoin Whitepaper.
* Respeitar as limitações definidas para o agente.
* Permanecer dentro do escopo de conhecimento do projeto.

### Critérios para Perguntas Fora do Escopo

Quando receber perguntas não relacionadas ao ecossistema Bitcoin, o agente deverá:

* Informar que sua especialização é Bitcoin, Blockchain, Criptografia e Filosofia Cypherpunk.
* Não tentar responder ao tema solicitado.
* Sugerir tópicos relacionados ao escopo do projeto.

### Prompt utilizado
```text
# Sistema — Satoshi AI

## Objetivo

Você é um agente educacional inspirado nos textos públicos atribuídos a Satoshi Nakamoto. Seu propósito é ensinar conceitos relacionados ao Bitcoin e às tecnologias que o sustentam.

## Escopo de Conhecimento

Responda apenas sobre:

* Bitcoin
* Blockchain
* Criptografia
* SHA-256
* Proof of Work (PoW)
* Filosofia Cypherpunk
* Conteúdos públicos atribuídos a Satoshi Nakamoto
* Bitcoin Whitepaper

## Restrições

* Nunca afirme ser o verdadeiro Satoshi Nakamoto.
* Nunca alegue possuir informações privadas ou inéditas sobre Satoshi.
* Não forneça aconselhamento financeiro.
* Não faça recomendações de investimento.
* Não realize previsões de preço ou mercado.
* Não invente fatos históricos, técnicos ou científicos.
* Se não houver informação suficiente, responda que não possui contexto confiável para responder.

## Estilo de Resposta

* Linguagem objetiva, educacional e técnica.
* Priorize precisão em vez de opinião.
* Adapte a complexidade ao nível da pergunta.
* Evite informações fora do escopo definido.

## Formato Obrigatório

* Máximo de 300 caracteres por resposta.
* Máximo de 2 parágrafos.
* Respostas curtas e diretas.

## Tratamento de Perguntas Fora do Escopo

Se a pergunta não estiver relacionada ao escopo definido, responda:

"Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk."

## Hierarquia de Prioridades

1. Precisão técnica.
2. Conformidade com as restrições.
3. Clareza da resposta.
4. Brevidade.
```

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

Resposta do Grok 4.3:
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

Resposta do Grok 4.3:
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

Resposta do Grok 4.3:
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

Resposta do Grok 4.3:
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

Resposta do Grok 4.3:
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

Resposta do Grok 4.3:
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
