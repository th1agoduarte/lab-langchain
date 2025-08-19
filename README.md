# 🤖 Projeto LangChain - Python

Este projeto utiliza **LangChain** integrado com **Google Generative AI** e **OpenAI** para construção de aplicações de IA.  

---

## 📦 Pré-requisitos

- 🐍 Python **3.10+**
- 📌 `pip` atualizado  
- 🔑 Conta no **Google AI Studio** (para API GenAI)  
- 🔑 Conta na **OpenAI** (para GPT-4/GPT-4o/embeddings)  

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/th1agoduarte/lab-langchain
cd langchain-projeto
pip install -r requirements.txt
```

---

## 📚 Requirements

No arquivo `requirements.txt` devem estar, no mínimo:

```txt
langchain
langchain-community
langchain-openai
langchain-google-genai
python-dotenv
```

> 💡 Opcional: `jupyter`, `notebook` caso queira rodar experimentos interativos.

---

## 🔑 Configuração das API Keys

### 🟦 OpenAI
1. Crie uma conta (ou acesse) em [OpenAI](https://platform.openai.com).  
2. Vá até **View API Keys** em [API Keys](https://platform.openai.com/account/api-keys).  
3. Copie a chave e adicione no arquivo `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
```

---

### 🟨 Google Generative AI (Gemini)
1. Acesse [Google AI Studio](https://aistudio.google.com/).  
2. Clique em **Get API Key**.  
3. Copie a chave e adicione no arquivo `.env`:

```env
GOOGLE_API_KEY=AIzaSyAxxxxxxxxxxxx
```

---

## 🔧 Como usar

Carregue as chaves no Python usando `dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
```

Exemplo de inicialização com LangChain:

```python
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# OpenAI
llm_openai = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)

# Google Generative AI
llm_google = ChatGoogleGenerativeAI(model="gemini-pro", api_key=google_key)

response = llm_openai.invoke("Hello, world with OpenAI!")
print("🔵 OpenAI:", response)

response = llm_google.invoke("Hello, world with Google GenAI!")
print("🟡 Google GenAI:", response)
```

---

## ✅ Próximos passos
- 📓 Criar exemplos práticos em `notebooks/`  
- 🔗 Integrar ferramentas externas no LangChain (retrievers, bancos de dados, APIs)  
- 🤖 Montar pipelines de agentes  

---
