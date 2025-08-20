from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, I'm {name}!  Tell me a joke with my name!",
)

text = template.format(name="Thiago")
print(text)  # Output: Hi, I'm Thi