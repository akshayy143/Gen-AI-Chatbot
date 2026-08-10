
# from langchain.chat_models import init_chat_model

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")  # Initialize the chat model

# response = model.invoke("Why do parrots talk?")

# print(response)  # Print the response from the model
import os
from langchain.chat_models import init_chat_model

os.environ["GOOGLE_API_KEY"] = ""

model = init_chat_model("google_genai:gemini-3.5-flash-lite")

response = model.invoke("Why do human talk?")
print(response.content)