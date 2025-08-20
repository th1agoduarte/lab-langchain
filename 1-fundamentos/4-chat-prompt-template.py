from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

system = ("system", "you are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

menssages = chat_prompt.format_messages(
    style="funny",
    question="who is Allan Turing?"
)

for message in menssages:
    print(f"{message.type}: {message.content}")

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)
result = model.invoke(menssages)
print(result.content)  # Output: A funny answer about Allan Turing
# Note: The output will depend on the model's response and may vary each time you run it.