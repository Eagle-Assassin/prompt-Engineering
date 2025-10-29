from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#human message ->msg sent by human to AI
#AI message-> msg sent by AI
#System message-> Message kept at the start befor sending
load_dotenv()
model= ChatOpenAI()

messages= [
    SystemMessage(content="You are ahelpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)