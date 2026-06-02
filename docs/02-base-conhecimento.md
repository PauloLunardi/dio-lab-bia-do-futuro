# Base de Conhecimento

## Dados Utilizados

Os dados do agente são armazenados localmente na pasta `/data` e estruturados em formatos JSON e TXT. Cada fonte possui uma função específica dentro do sistema de RAG (Retrieval-Augmented Generation).

| Arquivo | Formato | Tipo de Dado | Utilização no Agente |
|---------|---------|--------------|----------------------|
| [`bitcoin_whitepaper.txt`](/data/knowledge_base/bitcoin_whitepaper.txt) | TXT | Técnico/Primário | Fonte oficial do protocolo Bitcoin utilizada como referência técnica e histórica |
| [`bitcoin_dataset.json`](/data/raw/bitcoin_dataset.json) | JSON | Educacional | Dataset com conceitos fundamentais do Bitcoin utilizado para respostas introdutórias e educacionais |
| [`celestia_dataset.json`](/data/raw/celestia_dataset.json) | JSON | Filosófico | Conteúdo relacionado à descentralização, cultura cypherpunk e visão associada ao ecossistema Bitcoin |
| [`sha256_bounded.json`](/data/raw/sha256_bounded.json) | JSON | Técnico | Dataset sobre propriedades e aprendizado relacionado ao algoritmo SHA-256 |
| [`sha256_dynamics.json`](/data/raw/sha256_dynamics.json) | JSON | Técnico | Dataset complementar para estudo do comportamento e dinâmica do SHA-256 |
| [`sha256_probe.json`](/data/raw/sha256_probe.json) | JSON | Técnico | Dataset complementar para exploração avançada de características do SHA-256 |
| [`bitcoin_knowledge.json`](/data/processed/bitcoin_knowledge.json) | JSON | Conhecimento Processado | Base estruturada para recuperação contextual (RAG) sobre Bitcoin |
| [`cypherpunk_knowledge.json`](/data/processed/cypherpunk_knowledge.json) | JSON | Conhecimento Processado | Base estruturada para respostas sobre filosofia cypherpunk e descentralização |
| [`cryptography_advanced.json`](/data/processed/cryptography_advanced.json) | JSON | Conhecimento Processado | Base estruturada para respostas avançadas sobre criptografia e SHA-256 |

> Esses arquivos compõem a base de conhecimento do agente e são utilizados em um pipeline de RAG, garantindo respostas contextualizadas e reduzindo alucinações.

---

## Adaptações nos Dados

- Os dados foram coletados de múltiplas fontes, incluindo datasets do Hugging Face, whitepaper oficial do Bitcoin e materiais audiovisuais.
- Todos os conteúdos foram padronizados para formatos JSON e TXT, facilitando o processamento e recuperação.
- As informações foram segmentadas por domínio (técnico, educacional e filosófico) para melhorar a qualidade da recuperação semântica.
- O conteúdo passa por pré-processamento com divisão em chunks para geração de embeddings e indexação vetorial.

---

## Estratégia de Integração

### Como os dados são carregados?

- Os dados são carregados localmente a partir da pasta `/data`.
- Durante a inicialização do sistema, os arquivos são processados e indexados para busca semântica.

### Como os dados são usados no sistema?

- O sistema utiliza uma arquitetura de RAG (Retrieval-Augmented Generation).
- As perguntas do usuário são convertidas em embeddings.
- Um mecanismo de similaridade vetorial recupera os trechos mais relevantes da base de conhecimento.
- Apenas os chunks mais relevantes são inseridos no prompt da IA para geração da resposta.

---

## Exemplo de Contexto Montado

### Consulta do usuário:
"O que é Bitcoin e como funciona mineração?"

### Contexto recuperado da base de conhecimento:

- Fonte: Bitcoin Whitepaper  
  - Tema: Proof of Work  
  - Trecho: "A proof-of-work chain is a solution to the double-spending problem..."  
  - Score de relevância: 0.91  

- Fonte: Dataset Bankless  
  - Tema: Filosofia do Bitcoin  
  - Trecho: "Bitcoin enables a decentralized monetary system without trusted intermediaries..."  
  - Score de relevância: 0.84  

- Fonte: Glossário interno  
  - Termo: Mining  
  - Definição: Processo de validação de blocos através de SHA-256  
  - Score de relevância: 0.88  

### Prompt enviado ao agente:

> Com base no contexto recuperado acima, responda como Satoshi Nakamoto explicaria de forma educacional, objetiva e com linguagem cypherpunk.
