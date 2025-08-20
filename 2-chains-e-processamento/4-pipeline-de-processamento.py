from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}```",
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```\n\n",
)

llm_en = ChatOpenAI(model="gpt-5-mini", temperature=0)

translate = template_translate | llm_en | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

result = pipeline.invoke({"initial_text": "LangChain é uma biblioteca poderosa para construir aplicações de IA."})

print(result)
