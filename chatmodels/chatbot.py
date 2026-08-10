import os
from langchain.chat_models import init_chat_model

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ["GOOGLE_API_KEY"] = "Q"

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

messages = [
    SystemMessage(content="You are a funny AIagent"),
]

print("------------ welcome to Gen AI Chatbot -------------")
while True:
    
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :",response.content)

print(messages)

