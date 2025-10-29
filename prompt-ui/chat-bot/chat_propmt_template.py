from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template=ChatPromptTemplate([
    ('system',"you are a helpful {domain} expert"),
    ("human","Explain in simple terms, ehat is {topic}")
    # SystemMessage(content="you are a helpful {domain} expert"                  ),
    # HumanMessage(content="Explain in simple terms, ehat is {topic}")
],)

prompt = chat_template.invoke({"domain":'crickrt',"topic":'Dusra'})

print(prompt)