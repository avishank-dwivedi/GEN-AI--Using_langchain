from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

chat_template = ChatPromptTemplate([
    ('system', ' you are elpful {domain} expert'),
    ('human', 'explain in simple term what is {topic} ?')
])
prompt = chat_template.invoke({'domain': "cricket", 'topic': "Dusra"})
print(prompt)