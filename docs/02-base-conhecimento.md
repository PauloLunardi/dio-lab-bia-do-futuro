# Base de Conhecimento

## Prompt usado para esta etapa:
> [!TIP]
>
> Me ajude a documentar a base de conhecimento do agente Satoshi AI. A base utiliza datasets do Hugging Face, conteúdos sobre Bitcoin, criptografia, filosofia cypherpunk e o Bitcoin Whitepaper. Preciso documentar fontes de dados, estrutura de pastas, processamento dos dados, estratégia de integração, carregamento dos arquivos e exemplos de contexto utilizado pela IA.
>

## Dados Utilizados

Os dados do agente são armazenados localmente na pasta [`/data`](/data) e estruturados em formatos JSON e TXT. Cada fonte possui uma função específica dentro do mecanismo de contextualização utilizado pelo agente.

A estrutura foi preparada para futura evolução para uma arquitetura RAG (Retrieval-Augmented Generation), porém a versão atual utiliza carregamento local dos arquivos para construção do contexto enviado ao modelo.

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

> Esses arquivos compõem a base de conhecimento do agente e são utilizados no processo de contextualização das respostas, garantindo maior alinhamento com as fontes disponíveis e reduzindo alucinações.

---

## Adaptações nos Dados

- Os dados foram coletados de múltiplas fontes, incluindo datasets do Hugging Face, whitepaper oficial do Bitcoin e materiais audiovisuais.
- Todos os conteúdos foram padronizados para formatos JSON e TXT, facilitando o processamento e recuperação.
- As informações foram segmentadas por domínio (técnico, educacional e filosófico) para melhorar a qualidade da recuperação semântica.
- O conteúdo é estruturado para permitir divisão em chunks, geração de embeddings e indexação vetorial durante a implementação completa da arquitetura RAG.

---

## Estrutura da Base de Conhecimento

```text
data/
├── raw/
│   ├── bitcoin_dataset.json
│   ├── celestia_dataset.json
│   ├── sha256_bounded.json
│   ├── sha256_dynamics.json
│   └── sha256_probe.json
│
├── processed/
│   ├── bitcoin_knowledge.json
│   ├── cypherpunk_knowledge.json
│   └── cryptography_advanced.json
│
└── knowledge_base/
    └── bitcoin_whitepaper.txt
```
---
## Estratégia de Integração

### Como os dados são carregados?

- Os dados podem ser encontrados localmente a partir da pasta [`/data`](/data).
- O agente não consome diretamente os datasets originais. Antes da utilização, os dados passam por uma etapa de processamento e estruturação para otimizar o consumo pela IA.
- Após o processamento, os arquivos estruturados são carregados pela aplicação e disponibilizados para construção do contexto enviado ao modelo.

#### Exemplo de carregamento dos dados:
```python
import json

with open(
    "data/processed/bitcoin_knowledge.json",
    "r",
    encoding="utf-8"
) as f:
    bitcoin_knowledge = json.load(f)

with open(
    "data/processed/cryptography_advanced.json",
    "r",
    encoding="utf-8"
) as f:
    cryptography_advanced = json.load(f)

with open(
    "data/processed/cypherpunk_knowledge.json",
    "r",
    encoding="utf-8"
) as f:
    cypherpunk_knowledge = json.load(f)

with open(
    "data/knowledge_base/bitcoin_whitepaper.txt",
    "r",
    encoding="utf-8"
) as f:
    whitepaper = f.read()
```

### Fluxo de Integração dos Dados

```text
            Fontes de Conhecimento
┌─────────────────────────┬──────────────────────────┐
│   Datasets Hugging Face │    Bitcoin Whitepaper    │
└─────────────┬───────────┴──────────────┬───────────┘
              │                          │
              ▼                          ▼

                   data/raw/
              ├── bitcoin_dataset.json
              ├── celestia_dataset.json
              └── sha256_*.json
                         │
                         ▼

            Processamento de Dados (Pandas + Python)
                         │
                         ▼

            JSON Estruturado para IA

                 data/processed/
              ├── bitcoin_knowledge.json
              ├── cypherpunk_knowledge.json
              └── cryptography_advanced.json
                         │
                         ▼

            Carregamento da Aplicação
                         │
                         ▼

            Construção do Prompt
                         │
                         ▼

            Resposta do Satoshi AI

      ├── Fonte Complementar de Conhecimento

            data/knowledge_base/
            └── bitcoin_whitepaper.txt
```


Essa abordagem permite separar as fontes originais dos dados processados, facilitando a manutenção, expansão da base de conhecimento e futura evolução para arquiteturas de RAG.


### Como os dados são usados no prompt?

- O sistema utiliza uma abordagem de recuperação contextual baseada em arquivos locais.
- Os conteúdos são armazenados em arquivos JSON e TXT dentro da pasta data/.
- Quando uma pergunta é recebida, o sistema consulta a base de conhecimento para identificar informações relacionadas ao tema solicitado.
- Os trechos relevantes são adicionados ao contexto enviado para a IA, auxiliando na geração de respostas mais precisas e alinhadas às fontes disponíveis.

#### Consulta do usuário

> Pergunta: Como funciona a mineração do Bitcoin e qual o papel do SHA-256?

##### Contexto Recuperado da Base de Conhecimento

**Arquivo:** `bitcoin_knowledge.json`

```text
Tema: Bitcoin Básico

- Bitcoin utiliza um mecanismo de consenso chamado Proof of Work.
- Os mineradores competem para validar novos blocos.
- A mineração protege a rede e impede gastos duplos.
```

**Arquivo:** `cryptography_advanced.json`

```text
Tema: Criptografia

- SHA-256 é o algoritmo de hash utilizado pelo Bitcoin.
- O hash transforma dados em uma sequência única de caracteres.
- Pequenas alterações na entrada geram hashes completamente diferentes.
```

**Arquivo:** `cypherpunk_knowledge.json`

```text
Tema: Filosofia Cypherpunk

- A descentralização reduz a dependência de autoridades centrais.
- A criptografia é utilizada para garantir segurança e soberania digital.
```

**Arquivo:** `bitcoin_whitepaper.txt`

```text
Fonte Primária

- O Proof of Work é utilizado para resolver o problema do gasto duplo.
- A cadeia de blocos permite consenso distribuído sem uma entidade central.
```

##### Prompt Enviado ao Agente

```text
Você é Satoshi AI.

Utilize o contexto abaixo para responder de forma educacional,
técnica e alinhada à filosofia cypherpunk.

[bitcoin_knowledge.json]
- Bitcoin utiliza Proof of Work...
- Mineradores validam blocos...

[cryptography_advanced.json]
- SHA-256 é utilizado para gerar hashes...

[cypherpunk_knowledge.json]
- Criptografia garante soberania digital...

[bitcoin_whitepaper.txt]
- Proof of Work resolve o problema do gasto duplo...
```

---

## Exemplo de Contexto Montado

### Consulta do usuário:
"O que é Bitcoin e como funciona mineração?"

### Contexto recuperado da base de conhecimento:

- Fonte: Bitcoin Whitepaper  
  - Tema: Proof of Work  
  - Trecho: "A proof-of-work chain is a solution to the double-spending problem..."  
  - Score de relevância: 0.91 (valor fictício utilizado apenas para exemplificar uma futura recuperação semântica)

- Fonte: Dataset Bankless  
  - Tema: Filosofia do Bitcoin  
  - Trecho: "Bitcoin enables a decentralized monetary system without trusted intermediaries..."  
  - Score de relevância: 0.84 (valor fictício utilizado apenas para exemplificar uma futura recuperação semântica)

- Fonte: Glossário interno  
  - Termo: Mining  
  - Definição: Processo de validação de blocos através de SHA-256  
  - Score de relevância: 0.88 (valor fictício utilizado apenas para exemplificar uma futura recuperação semântica)

### Prompt enviado ao agente:

> Com base no contexto recuperado acima, responda como Satoshi Nakamoto explicaria de forma educacional, objetiva e com linguagem cypherpunk.

## Implementação Atual

A versão atual do Satoshi AI utiliza carregamento local dos arquivos da base de conhecimento.

Durante cada consulta, os arquivos processados e o trecho do Bitcoin Whitepaper são carregados e incorporados ao contexto enviado ao modelo Qwen3:4B executado localmente através do Ollama.

Essa abordagem foi adotada para simplificar a implementação do MVP e garantir respostas fundamentadas em uma base de conhecimento controlada.

A estrutura dos dados foi organizada para permitir futura evolução para uma arquitetura RAG com embeddings, recuperação semântica e banco vetorial.
