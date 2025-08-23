# 🤖 Projeto de Estudos com LangChain

Este repositório contém uma coleção de exemplos e estudos práticos sobre o uso do **LangChain** com Python, integrado com as APIs da **OpenAI** e **Google Generative AI** para construir aplicações de IA.

---

## 📚 Estrutura do Projeto e Conteúdo

O projeto está organizado em diretórios que representam diferentes estágios de aprendizado com LangChain:

-   **`1-fundamentos/`**: Conceitos básicos, como inicializar modelos de linguagem (LLMs), criar e usar `PromptTemplates` e `ChatPromptTemplates`.
-   **`2-chains-e-processamento/`**: Foco na construção de pipelines (chains) usando a LangChain Expression Language (LCEL), `Runnables`, e estratégias de processamento de texto, como sumarização com `MapReduce`.
-   **`3-agentes-e-tools/`**: Implementação de agentes autônomos que utilizam ferramentas (`Tools`) para executar tarefas complexas, explorando o padrão ReAct.
-   **`4-gerenciamento-de-memoria/`**: Técnicas para adicionar memória a chatbots, permitindo que eles se lembrem de interações passadas, como `InMemoryChatMessageHistory` e `Sliding Window`.

---

## 📦 Pré-requisitos

-   🐍 Python **3.10+**
-   📌 `pip` atualizado
-   🔑 Conta no **Google AI Studio** (para API GenAI)
-   🔑 Conta na **OpenAI** (Para API GPT)

---

## ⚙️ Instalação

1.  Clone o repositório e navegue até o diretório:
    ```bash
    git clone https://github.com/th1agoduarte/lab-langchain
    cd lab-langchain
    ```

2.  Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

---

## 📚 Requirements

O arquivo `requirements.txt` deve conter, no mínimo:

```txt
# filepath: requirements.txt
langchain
langchain-core
langchain-community
langchain-openai
langchain-google-genai
python-dotenv
```

> 💡 **Opcional**: Adicione `jupyter` e `notebook` caso queira rodar experimentos interativos.

---

## 🔑 Configuração das API Keys

1.  Crie um arquivo chamado `.env` na raiz do projeto.
2.  Adicione suas chaves de API, como no exemplo abaixo:

    ```env
    # filepath: .env
    OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
    GOOGLE_API_KEY="AIzaSyAxxxxxxxxxxxx"
    ```

O código nos exemplos já está configurado para carregar essas variáveis de ambiente automaticamente.

---
## 🔧 Como Usar

Cada diretório contém scripts Python numerados que podem ser executados individualmente. Comece pelos exemplos em `1-fundamentos/` e avance conforme sua necessidade.

Exemplo básico de inicialização:

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa os modelos
llm_openai = ChatOpenAI(model="gpt-4o-mini")
llm_google = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Envia um prompt para cada modelo
response_openai = llm_openai.invoke("Qual a capital do Brasil?")
print("🔵 OpenAI:", response_openai.content)

response_google = llm_google.invoke("Qual a capital do Brasil?")
print("🟡 Google GenAI:", response_google.content)
```

---

## ✅ Próximos passos
- 📓 Criar exemplos práticos em `notebooks/`  
- 🔗 Integrar ferramentas externas no LangChain (retrievers, bancos de dados, APIs)  
- 🤖 Montar pipelines de agentes  
