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

### Prompt utilizado (ChatGPT, Copilot, Grok, Gemini)
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

### Prompt utilizado (₿ Satoshi AI)
```text
considere as informações abaixo para as proximas perguntas

Máximo de 300 caracteres por resposta.
Máximo de 2 parágrafos.
Respostas curtas e diretas.
```

## Cenários de Teste

### Teste 1: 
- **Nível:** Introdução
- **Objetivo:** Verificar se o modelo compreende e respeita as instruções iniciais(prompt acima) do sistema.
- **Resposta esperada:** Que a IAs assumam seu papel e as retrições para os testes.

Resposta do Satoshi AI:
```text
O Bitcoin propõe um sistema de cash peer-to-peer que resolve o duplo gasto sem terceiros, usando cadeia de blocos com hash e proof-of-work. A rede garante segurança e integridade.

A solução permite transações diretas entre usuários, validando transações com a maioria da potência computacional da rede, evitando instituições financeiras.
```
Resultado: 
- [ ] Correto
- [ ] Incorreto
- [x] Parcialmente Correto

Resposta do ChatGPT:
```text
Posso atuar nesta conversa seguindo esse comportamento:

Foco em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk.
Respostas curtas, técnicas e educacionais.
Sem aconselhamento financeiro ou previsões de mercado.
Sem alegar ser o verdadeiro Satoshi Nakamoto.

Faça sua próxima pergunta dentro desse escopo.
```
Resultado: 
- [x] Correto
- [ ] Incorreto
- [ ] Parcialmente Correto

Resposta do Copilot:
```text
O Bitcoin é um sistema de dinheiro eletrônico peer-to-peer descrito por Satoshi Nakamoto em 2008. Ele elimina intermediários, permitindo transações diretas entre usuários, registradas em uma blockchain.

A segurança vem do Proof of Work, que exige cálculos intensivos usando SHA-256. Essa abordagem reflete a filosofia Cypherpunk, defendendo privacidade e liberdade através da criptografia.
```
Resultado: 
- [ ] Correto
- [ ] Incorreto
- [x] Parcialmente Correto

Resposta do Grok:
```text
Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk. Pronto para explicar conceitos do whitepaper ou textos públicos atribuídos a Satoshi Nakamoto. Qual sua pergunta?
```
Resultado: 
- [x] Correto
- [ ] Incorreto
- [ ] Parcialmente Correto

Resposta do Gemini:
```text
Entendido. Assumo o papel de agente educacional baseado nos conceitos do Bitcoin e na filosofia Cypherpunk. Minhas respostas serão estritamente técnicas, diretas e limitadas ao escopo estabelecido, respeitando o teto de 300 caracteres e o formato de no máximo dois parágrafos.

Como posso ajudar você a entender o funcionamento do Bitcoin hoje?
```
Resultado: 
- [x] Correto
- [ ] Incorreto
- [ ] Parcialmente Correto

### Teste 2: 
- **Nível:** Iniciante
- **Pergunta:** "O que é Bitcoin?"
- **Resposta esperada:** Bitcoin é uma moeda digital descentralizada que permite transferências de valor sem intermediários.

Resposta do Satoshi AI:
```text
Bitcoin é uma moeda digital descentralizada que permite transações diretas entre usuários sem instituições financeiras, resolvendo o duplo gasto por meio de blockchain e prova de trabalho.
```

Resposta do ChatGPT:
```text
Bitcoin é um sistema de dinheiro eletrônico peer-to-peer descrito por Satoshi Nakamoto em 2008. Ele permite transferir valor diretamente entre participantes sem depender de uma autoridade central.

Sua segurança é baseada em criptografia, SHA-256 e Proof of Work, com registros armazenados em uma blockchain distribuída e verificável por qualquer participante da rede.
```

Resposta do Copilot:
```text
Bitcoin é um sistema de dinheiro eletrônico peer-to-peer criado em 2008. Ele permite transações diretas entre usuários sem intermediários, registradas em uma blockchain pública e imutável.

Sua segurança depende do Proof of Work com SHA-256, garantindo integridade e resistência à censura, alinhado à filosofia Cypherpunk.
```

Resposta do Grok:
```text
Bitcoin é um sistema de dinheiro eletrônico peer-to-peer, conforme o whitepaper de Satoshi Nakamoto (2008). Ele permite transações diretas entre usuários sem intermediários, usando blockchain, Proof of Work e SHA-256 para registro distribuído e segurança.
```

Resposta do Gemini:
```text
O Bitcoin é um sistema de dinheiro eletrônico de par para par (peer-to-peer), sem a necessidade de uma instituição financeira central.

Ele utiliza criptografia e uma rede descentralizada com Proof of Work para registrar transações de forma segura e imutável em um livro-razão público chamado blockchain.
```

Resultado: 
- [x] Correto
- [ ] Incorreto

### Teste 3:
- **Nível:** Intermediário
- **Pergunta:** "Como funciona a mineração do Bitcoin?"
- **Resposta esperada:** A mineração utiliza o mecanismo Proof of Work para validar blocos e proteger a rede Bitcoin através da resolução de desafios criptográficos.

Resposta do Satoshi AI:
```text
Mineração Bitcoin: mineiros resolvem puzzles criptográficos para validar transações e adicionar blocos. A primeira solução recebe Bitcoin. Prova de trabalho garante segurança e impede duplo gastamento.
```

Resposta do ChatGPT:
```text
A mineração é o processo que usa Proof of Work para validar blocos de transações e protegê-los contra alterações.

Mineradores calculam hashes SHA-256 até encontrar um resultado válido. O primeiro a encontrar adiciona o bloco à blockchain e recebe a recompensa definida pelo protocolo.
```

Resposta do Copilot:
```text
A mineração de Bitcoin consiste em validar blocos de transações através do Proof of Work. Mineradores competem para resolver cálculos complexos usando SHA-256.

O primeiro a encontrar o hash válido adiciona o bloco à blockchain, recebendo a recompensa. Esse processo garante segurança, descentralização e resistência à censura.
```

Resposta do Grok:
```text
A mineração é o mecanismo de Proof of Work do Bitcoin. Mineradores competem para encontrar um nonce que, ao ser hashado com SHA-256 junto aos dados do bloco, produza um hash com valor inferior ao alvo de dificuldade atual.O primeiro que encontra e valida o bloco o propaga na rede, recebendo a recompensa de subsídio + taxas. Isso protege a rede e mantém o consenso distribuído.
```

Resposta do Gemini:
```text
A mineração funciona através do Proof of Work (PoW). Mineradores usam poder computacional para resolver um quebra-cabeça matemático complexo baseado no algoritmo SHA-256.

O primeiro a encontrar a solução válida ganha o direito de transmitir o novo bloco para a rede e recebe uma recompensa em bitcoins.
```
Resultado: 
- [x] Correto
- [ ] Incorreto

### Teste 4:
- **Nível:** Técnico
- **Pergunta:** "Qual é o papel do SHA-256 na blockchain do Bitcoin?"
- **Resposta esperada:** O SHA-256 é a função hash utilizada para garantir integridade dos dados, encadear blocos e realizar o processo de mineração do Bitcoin.

Resposta do Satoshi AI:
```text
SHA-256 é usado em Bitcoin para gerar hashes únicos de cada bloco, garantindo integridade e imutabilidade. Essa função é essencial na prova de trabalho, tornando alterações não autorizadas computacionalmente inviáveis.
```

Resposta do ChatGPT:
```text
O SHA-256 é a função hash usada pelo Bitcoin para gerar identificadores únicos de blocos e transações, além de sustentar o mecanismo de Proof of Work.

Pequenas alterações nos dados produzem hashes completamente diferentes, permitindo verificar integridade e dificultando a adulteração da blockchain.
```

Resposta do Copilot:
```text
O SHA-256 é o algoritmo de hash usado no Bitcoin. Ele transforma dados em um valor fixo de 256 bits, garantindo integridade e imutabilidade.

Na blockchain, cada bloco referencia o hash do anterior. Isso impede alterações, pois qualquer modificação mudaria o resultado do Proof of Work.
```

Resposta do Grok:
```text
O SHA-256 é a função de hash criptográfico principal do Bitcoin. Ele garante a integridade da blockchain ao ligar cada bloco ao anterior através do hash do bloco precedente.Também é usado no Proof of Work (busca por hash abaixo do alvo), em árvores Merkle de transações e na derivação de endereços a partir de chaves públicas.
```

Resposta do Gemini:
```text
O SHA-256 é uma função de hash criptográfica que garante a imutabilidade e a segurança da rede.

Ele transforma os dados dos blocos em um código fixo de 256 bits, usado para encadear os blocos sequencialmente e como base para o desafio matemático do Proof of Work.
```

Resultado: 
- [x] Correto
- [ ] Incorreto

### Teste 5: 
- **Nível:** Avançado
- **Pergunta:** "Como o Bitcoin resolve o problema do gasto duplo?"
- **Resposta esperada:** O Bitcoin utiliza blockchain, consenso distribuído e Proof of Work para impedir que uma mesma unidade monetária seja gasta mais de uma vez.

Resposta do Satoshi AI:
```text
Bitcoin resolve o gasto duplo com rede peer-to-peer que cria cadeia de blocos com prova de trabalho. A cadeia mais longa (gerada pela maioria do poder computacional) é irreversível, impedindo alterações sem recalcular toda a cadeia.
```

Resposta do ChatGPT:
```text
O Bitcoin resolve o gasto duplo usando uma blockchain pública e o mecanismo de Proof of Work para ordenar transações em uma única sequência verificável.

Após confirmada em blocos aceitos pela maioria do poder computacional da rede, uma transação torna-se economicamente difícil de reverter ou duplicar.
```

Resposta do Copilot:
```text
O Bitcoin evita o gasto duplo usando a blockchain, um registro público e imutável. Cada transação é validada por mineradores via Proof of Work.  

Uma vez confirmada, a transação é incluída em um bloco. Alterar ou duplicar exigiria refazer o SHA-256 de toda a cadeia, tornando o ataque impraticável.
```

Resposta do Grok:
```text
O Bitcoin resolve o gasto duplo através de uma blockchain pública com timestamps e Proof of Work.Transações são agrupadas em blocos encadeados por SHA-256. A rede adota a cadeia com maior Proof of Work como história válida, tornando o gasto duplo computacionalmente impraticável após confirmações.
```

Resposta do Gemini:
```text
O Bitcoin resolve o gasto duplo através de uma blockchain pública cronológica combinada com o Proof of Work.

A rede ordena e registra as transações em blocos com carimbos de data/hora (timestamps). Uma vez aceito pela maioria dos nós via consenso, o histórico se torna imutável e impede que a mesma moeda seja reutilizada.
```

Resultado: 
- [x] Correto
- [ ] Incorreto

### Teste 6: 
- **Nível:** Challenger
- **Pergunta:** "Como um node utiliza o conjunto UTXO para verificar se uma transação é válida?"
- **Resposta esperada:** Um node verifica se os inputs referenciam UTXOs existentes e não gastos, valida as assinaturas criptográficas e confirma que a soma dos inputs é maior ou igual à soma dos outputs antes de atualizar o conjunto UTXO.

Resposta do Satoshi AI:
```text
O node verifica se os inputs estão no UTXO (não gastos), se a soma dos inputs ≥ saídas e se as assinaturas são válidas.
```

Resposta do ChatGPT:
```text
Um node valida uma transação verificando se cada entrada referencia uma UTXO existente e ainda não gasta.

Ele também valida as assinaturas criptográficas, confirma que a soma das entradas é maior ou igual à soma das saídas e, se tudo estiver correto, atualiza o conjunto UTXO removendo as saídas gastas e adicionando as novas.
```

Resposta do Copilot:
```text
Um node mantém o conjunto UTXO, que lista todas as saídas de transações não gastas. Ao receber uma nova transação, ele verifica se as entradas referem UTXOs válidos e disponíveis.  

Se os UTXOs existirem e não tiverem sido usados, a transação é considerada válida e pode ser incluída na blockchain.
```

Resposta do Grok:
```text
Um node Bitcoin mantém o conjunto UTXO (Unspent Transaction Outputs), que lista todos os outputs não gastos.Para validar uma transação, o node verifica se todos os inputs referenciam UTXOs existentes e não gastos, valida as assinaturas criptográficas e confirma que o valor total dos inputs é igual ou superior ao dos outputs (sem criação de moeda).
```

Resposta do Gemini:
```text
Um nó consulta o banco de dados UTXO (Unspent Transaction Outputs) para verificar se as moedas de entrada de uma nova transação realmente existem e não foram gastas.

O nó valida se a soma dos valores de entrada é maior ou igual às saídas e se a assinatura digital do remetente confere com a chave pública do UTXO.
```
Resultado: 
- [x] Correto
- [ ] Incorreto

### Teste 7:
- **Nível:** Fora de Escopo
- **Pergunta:** "Quem venceu a Copa do Mundo de 2022?"
- **Resposta esperada:** O agente deve informar que é especializado em Bitcoin, blockchain, criptografia e filosofia cypherpunk, não possuindo foco em eventos esportivos.

Resposta do Satoshi AI:
```text
Argentina
```

Resposta do ChatGPT:
```text
Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk.
```

Resposta do Copilot:
```text
Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk.
```

Resposta do Grok:
```text
Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk.
```

Resposta do Gemini:
```text
"Este agente é especializado apenas em Bitcoin, Blockchain, Criptografia, SHA-256, Proof of Work e Filosofia Cypherpunk."
```

Resultado: 
- [ ] Correto
- [x] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**Conclusão geral:**
- Demonstrou conhecimento técnico consistente sobre Bitcoin.
- Falhou no tratamento de perguntas fora do escopo.
- Apresentou aderência parcial às instruções iniciais do sistema.

**O que funcionou bem:**
- O agente respondeu corretamente às perguntas relacionadas a Bitcoin, blockchain, Proof of Work e SHA-256.
- Demonstrou boa capacidade de síntese respeitando o limite de caracteres.
- Apresentou respostas tecnicamente coerentes com o Bitcoin Whitepaper.

**O que pode melhorar:**
- Melhorar a aderência às instruções iniciais do sistema.
- Reforçar o tratamento de perguntas fora do escopo.
- Implementar mecanismos que reduzam respostas genéricas quando o usuário não fizer perguntas diretamente relacionadas ao Bitcoin.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
  > A latência não foi utilizada como critério de comparação, pois os testes focaram na qualidade das respostas e não no desempenho computacional do modelo.
  > Nos testes não considerei o tempo de respostas, pois escolhi um modelo de 3.2Gb Qwen3:4b
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
